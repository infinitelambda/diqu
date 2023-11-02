import os
import string
from datetime import datetime
from typing import Any, List

from jira import JIRA
from pandas import DataFrame

from diqu.utils.log import logger
from diqu.utils.meta import ResultCode


def alert(data) -> ResultCode:
    r = JiraBoard().raise_incidents(data=data)
    if r == ResultCode.SUCCEEDED:
        logger.info("✅ Done > JIRA")
    return r


class JiraBoard:
    """JIRA Board management"""

    def __init__(self) -> None:
        """Initialization"""
        self.project_id = os.environ.get("JIRA_PROJECT_ID")
        self.incident_type = os.environ.get("JIRA_ISSUE_TYPE") or "Bug"
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

    def raise_incidents(self, data: DataFrame) -> ResultCode:
        """Create | Update the Incident tickets

        Args:
            data (DataFrame): Input incident data

        Returns:
            ResultCode: Result code
        """
        open_tickets_filter = string.Template(
            'project = "$project" '
            'AND statusCategory != "Done" '
            'AND summary ~ "$filter" '
            "ORDER BY created DESC"
        ).substitute(
            project=self.project_id,
            filter=os.environ.get("JIRA_OPEN_TICKETS_FILTER_BY_SUMMARY") or "dbt",
        )

        try:
            open_ticket_data = self.__get_tickets(jql_filter=open_tickets_filter)
            joined = open_ticket_data.merge(
                right=data, on="JIRA_TICKET_SUMMARY", how="outer"
            )

            self.__create_tickets(
                data=joined.loc[
                    (joined["JIRA_ISSUE_KEY"].isnull())
                    & (joined["TEST_STATUS"] != "pass")
                    & (joined["TEST_STATUS"] != "deprecated")
                ]
            )
            self.__update_tickets(
                data=joined.loc[
                    joined["JIRA_ISSUE_KEY"].notnull() & joined["TEST_STATUS"].notnull()
                ]
            )
        except Exception as e:
            logger.error(str(e))
            return ResultCode.FAILED

        return ResultCode.SUCCEEDED

    def __build_field_list(self, data: DataFrame) -> List[dict]:
        """Build JIRA ticket fields

        Args:
            data (DataFrame): Input as a list of the tickets

        Returns:
            List[dict]: List of ticket's fields
        """
        data = data.fillna(0)
        description_template = string.Template(
            "h2. Test: [ $test_id ] has failed with the following information:\n\n"
            "- *Test ID*: $test_id\n"
            "- *Latest Status*: $test_status\n\n"
            "- *Latest Run Timestamp*: $check_timestamp (UTC)\n"
            "- *Latest Run Failed Rate*: $failed_rate\n\n"
            "- *Previous statuses*: $prev_statuses\n"
            "- *Previous run timestamps (UTC)*: $prev_check_timestamps\n"
            "- *Previous # of failed records*: $prev_failed_counts\n"
            "- *Previous # of scanned records*: $prev_scanned_counts\n\n"
            "- *tag | DQ Issue Type*: $dq_issue_type\n"
            "- *tag | KPI Category*: $kpi_category\n\n"
            "h2. Jira automation process | modified at $current_datetime (UTC)"
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
                    dq_issue_type=row["DQ_ISSUE_TYPE"],
                    kpi_category=row["KPI_CATEGORY"],
                    current_datetime=datetime.utcnow(),
                ),
                summary=row["JIRA_TICKET_SUMMARY"],
                issuetype=dict(name=self.incident_type),
                project=dict(id=self.project_id),
                labels=[
                    "AutomaticAlert",
                    "diqu"
                    f"{str(row['DQ_ISSUE_TYPE']).replace(' ','_').replace('-','_')}",
                    f"{str(row['KPI_CATEGORY']).replace(' ','_').replace('-','_')}",
                ],
            )
            for _, row in data.iterrows()
        ]

    def __get_tickets(self, jql_filter: str = None, limit: int = 100) -> DataFrame:
        """Get open tickets in JIRA Board

        Args:
            jql_filter (str, optional): JQL filter on ticket title. Defaults to None.
            limit (int, optional): Specify no of tickets returned. Defaults to 100.

        Returns:
            DataFrame: Frame of Ticket No and Ticket Title
        """
        search_issues = self.conn.search_issues(jql_str=jql_filter, maxResults=limit)
        return DataFrame(
            {
                "JIRA_ISSUE_KEY": [str(x.key) for x in search_issues],
                "JIRA_TICKET_SUMMARY": [
                    str(x.fields.summary).strip() for x in search_issues
                ],
            }
        )

    def __create_tickets(self, data: DataFrame) -> Any:
        """Bulk creation of the input tickets' data

        Args:
            data (DataFrame): Input tickets' data

        Returns:
            Any: None or List of created issues
        """
        if data.empty:
            logger.info("No new incident(s) detected!")
            return None
        logger.info(f"Creating {len(data)} ticket(s) ...")
        return self.conn.create_issues(field_list=self.__build_field_list(data=data))

    def __update_tickets(self, data: DataFrame) -> Any:
        """Update the existing ticket in JIRA Board

        Args:
            data (DataFrame): Input tickets' data need updating

        Returns:
            Any:  None or List of updated issues
        """
        if data.empty:
            logger.info("No open incident(s) need updating!")
            return None
        logger.info(f"Updating {len(data)} ticket(s) ...")
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
