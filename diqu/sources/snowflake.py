import snowflake.connector
from pandas import DataFrame

from diqu.sources.base import BaseConnection


def get_connection(config: dict) -> BaseConnection:
    """Get the Snowflake connection

    Args:
        config (dict): Connection attributes

    Returns:
        BaseConnection: SnowflakeConnection
    """
    return SnowflakeConnection(**config)


class SnowflakeConnection(BaseConnection):
    """Snowflake connection class"""

    def __init__(self, **config) -> None:
        super().__init__(**config)

        clean_config = dict(
            account=self.get_profile_config("account"),
            user=self.get_profile_config("user"),
            password=self.get_profile_config("password"),
            role=self.get_profile_config("role"),
            warehouse=self.get_profile_config("warehouse"),
            database=self.get_profile_config("database"),
            schema=self.get_profile_config("schema"),
            session_parameters={"QUERY_TAG": "diqu.sources.snowflake"},
        )

        if self.config.get("authenticator"):
            clean_config.pop("password")
            clean_config["authenticator"] = "externalbrowser"
            clean_config["client_request_mfa_token"] = True

        if self.config.get("private_key") or self.config.get("private_key_path"):
            clean_config.pop("password")
            if self.config.get("private_key"):
                clean_config["private_key"] = self.get_profile_config("private_key")
            else:
                clean_config["private_key_path"] = self.get_profile_config(
                    "private_key_path"
                )
            clean_config["private_key_passphrase"] = self.get_profile_config(
                "private_key_passphrase"
            )

        self.conn = snowflake.connector.connect(**clean_config)

    def execute(self, query: str) -> DataFrame:
        cur = self.conn.cursor()
        try:
            cur.execute(query)
            df_result = cur.fetch_pandas_all()
        finally:
            cur.close()

        return df_result
