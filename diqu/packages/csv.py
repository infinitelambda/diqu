def get_query(config: dict) -> str:
    """Return CSV file name

    Args:
        config (dict): Configuration object

    Returns:
        str: CSV file name
    """
    return Csv(**config).get_query()


class Csv:
    """Package CSV class"""

    def __init__(self, **kwargs) -> None:
        """Initilization"""
        self.query_file = kwargs.get("query_file") or "csv__data.csv"

    def get_query(self) -> str:
        """Return the CSV file name

        Returns:
            str: CSV file name
        """
        return self.query_file
