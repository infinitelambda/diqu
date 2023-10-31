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
        return self.query.take(self.query.file or "dq_tools__get_test_results.sql")
