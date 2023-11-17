import os
import re
import string
from datetime import datetime
from typing import Any, List

from jira import JIRA
from pandas import DataFrame

from diqu.utils.log import logger
from diqu.utils.meta import ResultCode


def alert(data) -> ResultCode:
    r = JiraBoard().raise_issues(data=data)
    if r == ResultCode.SUCCEEDED:
        logger.info("✅ Done > JIRA")
    return r


class JiraBoard:
    """JIRA Board management"""

    def __init__(self) -> None:
        """Initialization"""
        self.project_id = os.environ.get("JIRA_PROJECT_ID")
        self.issue_type = os.environ.get("JIRA_ISSUE_TYPE") or "Bug"
        self.conn = self.get_connection()

    def get_connection(self) -> JIRA:
        """Return JIRA Board connection

        Returns:
            JIRA: Connection object
        """
        return JIRA(
            options={"server": os.environ.get("JIRA_SERVER")},
            basic_auth=(
                os.environ.get("JIRA_AUTH_USER"),
                os.environ.get("JIRA_AUTH_PASSWORD"),
            ),
        )

    def raise_issues(self, data: DataFrame) -> ResultCode:
        """Create | Update the Issue issues

        Args:
            data (DataFrame): Input issue data

        Returns:
            ResultCode: Result code
        """
        open_issues_filter = string.Template(
            'project = "$project" '
            'AND statusCategory != "Done" '
            'AND summary ~ "$filter" '
            "ORDER BY created DESC"
        ).substitute(
            project=self.project_id,
            filter=os.environ.get("JIRA_OPEN_ISSUES_FILTER_BY_SUMMARY") or "dq-tools",
        )

        try:
            open_issue_data = self.__get_issues(jql_filter=open_issues_filter)
            joined = open_issue_data.merge(right=data, on="TEST_ID", how="outer")
            self.__create_issues(
                data=joined.loc[
                    (joined["JIRA_ISSUE_KEY"].isnull())
                    & (joined["TEST_STATUS"] != "pass")
                    & (joined["TEST_STATUS"] != "deprecate")
                ]
            )
            self.__update_issues(
                data=joined.loc[
                    joined["JIRA_ISSUE_KEY"].notnull() & joined["TEST_STATUS"].notnull()
                ]
            )
        except Exception as e:
            logger.error(str(e))
            return ResultCode.FAILED

        return ResultCode.SUCCEEDED

    def __build_field_list(self, data: DataFrame) -> List[dict]:
        """Build JIRA issue fields

        Args:
            data (DataFrame): Input as a list of the issues

        Returns:
            List[dict]: List of issue's fields
        """
        data = data.fillna(0)
        description_template = string.Template(
            "h2. Test metadata:\n\n"
            "- *Test ID*: --- $test_id --- \n"
            "- *Latest Status*: $test_status\n\n"
            "- *Latest Run Timestamp*: $check_timestamp (UTC)\n"
            "- *Latest Run Failed Rate*: $failed_rate\n\n"
            "- *Previous statuses*: $prev_statuses\n"
            "- *Previous run timestamps (UTC)*: $prev_check_timestamps\n"
            "- *Previous # of failed records*: $prev_failed_counts\n"
            "- *Previous # of scanned records*: $prev_scanned_counts\n\n"
            "- *tag 1*: $tag_1\n"
            "- *tag 2*: $tag_2\n\n"
            "h2. Managed by diqu | modified at $current_datetime (UTC)"
        )
        return [
            dict(
                description=description_template.substitute(
                    test_id=row["TEST_ID"],
                    test_status=row["TEST_STATUS"],
                    check_timestamp=row["CHECK_TIMESTAMP"],
                    failed_rate=row["FAILED_RATE"],
                    prev_statuses=row["PREV_STATUSES"],
                    prev_check_timestamps=row["PREV_CHECK_TIMESTAMPS"],
                    prev_failed_counts=row["PREV_NO_OF_RECORDS_FAILED"],
                    prev_scanned_counts=row["PREV_NO_OF_RECORDS_SCANNED"],
                    tag_1=row["TAG_1"],
                    tag_2=row["TAG_2"],
                    current_datetime=datetime.utcnow(),
                ),
                summary=row["TEST_TITLE"],
                issuetype=dict(name=self.issue_type),
                project=dict(id=self.project_id),
                labels=[
                    "diqu",
                    f"{str(row['TAG_1']).replace(' ','_').replace('-','_')}",
                    f"{str(row['TAG_2']).replace(' ','_').replace('-','_')}",
                ],
            )
            for _, row in data.iterrows()
        ]

    def __get_issues(self, jql_filter: str = None, limit: int = 100) -> DataFrame:
        """Get open issues in JIRA Board

        Args:
            jql_filter (str, optional): JQL filter on issue summary. Defaults to None.
            limit (int, optional): Specify the number of issues returned. Defaults to 100.

        Returns:
            DataFrame: Frame of Ticket No and Ticket Title
        """
        search_issues = self.conn.search_issues(jql_str=jql_filter, maxResults=limit)
        regexp_str = "--- (.*) ---"  # test_id is wrapped between 2 '---'
        return DataFrame(
            {
                "JIRA_ISSUE_KEY": [str(x.key) for x in search_issues],
                "TEST_ID": [
                    re.search(regexp_str, str(x.fields.description)).group(1)
                    for x in search_issues
                    if re.search(regexp_str, str(x.fields.description)) is not None
                ],
            }
        )

    def __create_issues(self, data: DataFrame) -> Any:
        """Bulk creation of the input issues' data

        Args:
            data (DataFrame): Input issues' data

        Returns:
            Any: None or List of created issues
        """
        if data.empty:
            logger.info("No new issue(s) detected!")
            return None
        logger.info(f"Creating {len(data)} issue(s) ...")
        return self.conn.create_issues(field_list=self.__build_field_list(data=data))

    def __update_issues(self, data: DataFrame) -> Any:
        """Update the existing issue in JIRA Board

        Args:
            data (DataFrame): Input issues' data need updating

        Returns:
            Any:  None or List of updated issues
        """
        if data.empty:
            logger.info("No open issue(s) need updating!")
            return None
        logger.info(f"Updating {len(data)} issue(s) ...")
        results = []
        for _, row in data.iterrows():
            logger.info(f"Updating {row['JIRA_ISSUE_KEY']}...")
            fields_list = self.__build_field_list(
                data=data.loc[data["JIRA_ISSUE_KEY"] == row["JIRA_ISSUE_KEY"]]
            )[0]
            fields_list.pop("issuetype")
            results.append(
                self.conn.issue(row["JIRA_ISSUE_KEY"]).update(fields=fields_list)
            )

        return results
