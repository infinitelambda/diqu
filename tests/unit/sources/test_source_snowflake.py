from unittest import mock

import pytest

from diqu.sources import snowflake


class TestSourceSnowflake:
    @pytest.mark.parametrize(
        "config, clean_config",
        [
            (
                dict(authenticator="test"),
                dict(
                    account=None,
                    user=None,
                    role=None,
                    warehouse=None,
                    database=None,
                    schema=None,
                    session_parameters={"QUERY_TAG": "diqu.sources.snowflake"},
                    authenticator="externalbrowser",
                    client_request_mfa_token=True,
                ),
            ),
        ],
    )
    def test_get_snowflake_connection_with_authenticator(self, config, clean_config):
        with mock.patch("snowflake.connector.connect") as mock_connect:
            mock_con = mock_connect.return_value
            mock_cur = mock_con.cursor.return_value
            mock_cur.fetch_pandas_all.return_value = "data"
            actual = snowflake.get_connection(config=config).execute(query="x")
            assert actual == "data"
            mock_connect.assert_called_once_with(**clean_config)
