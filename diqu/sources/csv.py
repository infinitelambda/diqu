from pandas import DataFrame, read_csv

from diqu.sources.base import BaseConnection
from diqu.utils import exception


def get_connection(config: dict) -> BaseConnection:
    """Get the CSV connection

    Args:
        config (dict): Connection attributes

    Returns:
        BaseConnection: CsvConnection
    """
    return CsvConnection(**config)


class CsvConnection(BaseConnection):
    """CSV connection class"""

    def __init__(self, **config) -> None:
        super().__init__(**config)
        self.dir = self.get_profile_config("dir")

    def execute(self, query: str) -> DataFrame:
        """Read csv

        Args:
            query (str): Csv file name

        Returns:
            DataFrame: Csv content
        """
        with exception.handle_file_errors(query):
            return read_csv(f"{self.dir}/{query}")
