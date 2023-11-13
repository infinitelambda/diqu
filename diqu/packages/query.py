import os

from diqu.utils import exception
from diqu.utils.log import logger


class Query:
    """Query helper class"""

    def __init__(self, **kwargs) -> None:
        """Initilization:
        - Get query directory
        """
        self.dir = kwargs.get("query_dir")
        self.file = kwargs.get("query_file")
        self.database = kwargs.get("query_database")
        self.schema = kwargs.get("query_schema")
        if not self.dir:
            self.dir = f"{os.path.dirname(os.path.realpath(__file__))}/include"

    def take(self, file: str) -> str:
        """Scan the query directory and get the query string from file

        Args:
            file (str): SQL file name (without the extension `.sql`)

        Raises:
            click.FileError: Read file error

        Returns:
            str: SQL query string
        """
        query_file = f"{self.dir}/{file}"
        logger.info(f"Looking for the query in: {query_file}")
        with exception.handle_file_errors(query_file):
            with open(query_file, "r") as content:
                sql = content.read()
                if self.database:
                    sql = sql.replace("$database", self.database)
                else:
                    sql = sql.replace("$database.", "")  # assume current db

                if self.schema:
                    sql = sql.replace("$schema", self.schema)
                else:
                    sql = sql.replace("$schema.", "")  # assume current schema

                return sql
