import os
import string

from diqu.packages.query import Query
from diqu.utils.jira_variable_config import (
    JIRA_TICKET_DEPRECATED_WINDOW_IN_DAYS,
    JIRA_TICKET_UPDATE_WINDOW_IN_DAYS,
)


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
        deprecated_window = (
            JIRA_TICKET_DEPRECATED_WINDOW_IN_DAYS
            if JIRA_TICKET_DEPRECATED_WINDOW_IN_DAYS is not None
            else 3
        )
        update_window = (
            JIRA_TICKET_UPDATE_WINDOW_IN_DAYS
            if JIRA_TICKET_UPDATE_WINDOW_IN_DAYS is not None
            else 14
        )
        return string.Template(
            self.query.take(self.query.file or "dq_tools__get_test_results.sql")
        ).substitute(
            filter=os.environ.get("JIRA_OPEN_TICKETS_FILTER_BY_SUMMARY") or "dq-tools",
            deprecated_window_in_days=deprecated_window,
            update_window_in_days=update_window,
        )
