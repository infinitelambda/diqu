import os
import abc
import re

from pandas import DataFrame


class SingletonABCMeta(abc.ABCMeta):
    """Singleton Metaclass for ABC"""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonABCMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def clear(cls):
        cls._instances = {}


class BaseConnection(metaclass=SingletonABCMeta):
    """Abstract DWH Connection class"""

    def __init__(self, **config) -> None:
        self.config = config

    def get_profile_config(self, attr: str) -> str:
        """Get connection attribute value from profiles.yml file.

        Supporting the detect the ENV_VAR configuration.

        Args:
            attr (str): Attribute name

        Returns:
            str: Attribute value
        """
        attr_value = self.config.get(attr)
        if not attr_value:
            return None

        pattern = r"env_var\('([^']*)'\)"
        match = re.search(pattern, attr_value)
        if match:
            env_var = match.group(1)
            return os.environ.get(str(env_var))

        return attr_value

    @abc.abstractclassmethod
    def execute(self, query: str) -> DataFrame:
        """Execute the SQL query to the DWH and return the DataFrame result

        Args:
            query (str): SQL query
        """
