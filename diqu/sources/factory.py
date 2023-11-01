from pathlib import Path

from pandas import DataFrame

from diqu.utils import exception, yml
from diqu.utils.log import logger
from diqu.utils.module import load_module


class SourceFactory:
    """DWH Source Factory class"""

    def __init__(self, **kwargs) -> None:
        """Initilization:
        - Detect the connection configuration in the dbt profile.yml
        - Load DWH module and get the database connection
        """
        self.dbt_profile_dir = kwargs.get("profiles_dir") or (Path.home() / ".dbt")
        self.dbt_project_dir = kwargs.get("project_dir") or Path.cwd()

        dbt_profile_name = kwargs.get("profile_name") or yml.load(
            file_path=f"{self.dbt_project_dir}/dbt_project.yml"
        ).get("profile", "diqu")
        dbt_profile_file_path = f"{self.dbt_profile_dir}/profiles.yml"

        with exception.handle_config_errors(
            dbt_profile_file_path,
            f"Profile [{dbt_profile_name}] is not found or a fault config",
        ):
            dbt_profile_content = yml.load(file_path=dbt_profile_file_path).get(
                dbt_profile_name
            )

            connection_config = dbt_profile_content.get("outputs", {}).get(
                kwargs.get("target") or dbt_profile_content.get("target")
            )

            module_name = connection_config.get("type")
            self.connection = load_module(
                name=module_name, package="diqu.sources"
            ).get_connection(config=connection_config)
            logger.info(f"Using dbt profile: {dbt_profile_name}")
            logger.info(f"Using dbt profiles.yml at: {self.dbt_profile_dir}")
            logger.info(f"Using {module_name} connection")

    def execute(self, query: str) -> DataFrame:
        """Execute SQL query

        Args:
            query (str): SQL query

        Returns:
            DataFrame: Query result
        """
        return self.connection.execute(query=query)
