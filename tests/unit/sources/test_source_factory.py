from pathlib import Path
from unittest import mock

import click
import pytest

from diqu.sources import snowflake
from diqu.sources.factory import SourceFactory


class TestSourceFactory:
    @pytest.mark.parametrize(
        "kwargs",
        [
            (dict()),
        ],
    )
    def test_init_nok(self, kwargs):
        with pytest.raises(click.FileError):
            SourceFactory(**kwargs)

    @pytest.mark.parametrize(
        "kwargs, dbt_profile_dir, dbt_project_dir, dbt_profile_name, target",
        [
            (dict(), (Path.home() / ".dbt"), Path.cwd(), "diqu", None),
        ],
    )
    def test_init_ok(
        self, kwargs, dbt_profile_dir, dbt_project_dir, dbt_profile_name, target
    ):
        with mock.patch(
            "diqu.utils.yml.load", return_value=dict(data="irrelevant")
        ) as mock_load:
            factory = SourceFactory(**kwargs)
            assert factory.dbt_profile_dir == dbt_profile_dir
            assert factory.dbt_profile_name == dbt_profile_name
            assert factory.dbt_project_dir == dbt_project_dir
            assert factory.target == target

            mock_load.assert_called_once_with(
                file_path=f"{dbt_project_dir}/dbt_project.yml"
            )

    @pytest.mark.parametrize(
        "kwargs, dbt_profile_dir",
        [
            (dict(profile_name="diqu"), (Path.home() / ".dbt")),
            (dict(profile_name="diqu", profiles_dir="irrelevant"), "irrelevant"),
        ],
    )
    def test_get_connection(self, kwargs, dbt_profile_dir):
        with mock.patch(
            "diqu.utils.yml.load",
            return_value=dict(
                diqu=dict(outputs=dict(dev=dict(type="snowflake")), target="dev")
            ),
        ) as mock_load:
            with mock.patch(
                "diqu.sources.factory.load_module", return_value=snowflake
            ) as mock_load_module:
                with mock.patch(
                    "diqu.sources.snowflake.get_connection", return_value="irrelevant"
                ) as mock_get_connection:
                    _ = SourceFactory(**kwargs).get_connection()
        mock_load.assert_called_once_with(file_path=f"{dbt_profile_dir}/profiles.yml")
        mock_load_module.assert_called_once()
        mock_get_connection.assert_called_once()

    def test_get_connection_error_as_invalid_profile_file_path(self):
        with pytest.raises(click.FileError):
            SourceFactory(**dict(profiles_dir="invalid/path")).get_connection()

    def test_get_connection_error_as_invalid_profile_file_content(self):
        with mock.patch(
            "diqu.utils.yml.load",
            return_value=dict(
                diqu=dict(outputs=dict(dev=dict(type="snowflake")), target="dev")
            ),
        ) as mock_load:
            with mock.patch(
                "diqu.sources.factory.load_module", return_value=snowflake
            ) as mock_load_module:
                with pytest.raises(click.BadParameter):
                    SourceFactory(**dict(profile_name="diqu1")).get_connection()
        mock_load.assert_called_once_with(
            file_path=f"{(Path.home() / '.dbt')}/profiles.yml"
        )
        assert 0 == mock_load_module.call_count

    @mock.patch("diqu.utils.yml.load", return_value=dict(data="irrelevant"))
    @mock.patch.object(snowflake.SnowflakeConnection, "execute")
    @mock.patch.object(SourceFactory, "get_connection")
    def test_execute(self, mock_get_connection, mock_execute, mock_load):
        mock_get_connection.return_value = snowflake.SnowflakeConnection
        mock_execute.return_value = "data"
        assert "data" == SourceFactory().execute(query="irrelevant")
        mock_load.assert_called_once()
        mock_get_connection.assert_called_once()
        mock_execute.assert_called_once()
