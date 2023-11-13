import os
import string

from diqu.packages.query import Query


def get_query(config: dict) -> str:
    """Return SQL query

    Args:
        config (dict): Configuration object

    Returns:
        str: SQL query string
    """
    return DqTools(**config).get_query()


class DqTools:
    """Package dq-tools class"""

    def __init__(self, **kwargs) -> None:
        """Initilization: Get the query engine"""
        self.query = Query(**kwargs)

    def get_query(self) -> str:
        """Return the SQL query using the query engine

        Returns:
            str: SQL query string
        """
        return string.Template(
            self.query.take(self.query.file or "dq_tools__get_test_results.sql")
        ).substitute(
            filter=os.environ.get("JIRA_OPEN_ISSUES_FILTER_BY_SUMMARY") or "dq-tools",
            deprecated_window_in_days=os.environ.get("ISSUE_DEPRECATED_WINDOW_IN_DAYS")
            or "3",
            update_window_in_days=os.environ.get("ISSUE_UPDATE_WINDOW_IN_DAYS") or "14",
        )
