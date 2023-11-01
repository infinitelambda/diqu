from unittest import mock

import click
import pytest
from tests.integration.invocation import diquRunner

class TestRunner:
    @pytest.fixture
    def diqu(self) -> diquRunner:
        return diquRunner()

    def test_runner_unhandled_exception(self, diqu: diquRunner) -> None:
        with mock.patch(
            "diqu.cli.main.diqu.make_context", side_effect=click.exceptions.Exit(-1)
        ):
            with pytest.raises(Exception):
                diqu.invoke(["invalid_command"])

    # def test_group_invalid_option(self, diqu: diquRunner) -> None:
    #     with pytest.raises(Exception):
    #         diqu.invoke(["--invalid-option"])

    # def test_command_invalid_option(self, diqu: diquRunner) -> None:
    #     with pytest.raises(Exception):
    #         diqu.invoke(["run", "--invalid-option"])

    # def test_invalid_command(self, diqu: diquRunner) -> None:
    #     with pytest.raises(Exception):
    #         diqu.invoke(["invalid-command"])

    # def test_invoke_version(self, diqu: diquRunner) -> None:
    #     diqu.invoke(["--version"])

    # def test_invoke_help(self, diqu: diquRunner) -> None:
    #     diqu.invoke(["-h"])
    #     diqu.invoke(["--help"])

    # def test_invoke_debug(self, diqu: diquRunner) -> None:
    #     diqu.invoke(["debug"])

    # def test_invoke_run_with_invalid_artifact_path(self, diqu: diquRunner) -> None:
    #     with pytest.raises(click.exceptions.FileError):
    #         diqu.invoke(["run", "--artifacts-dir", "/path/invalid"])

    # def test_invoke_run_with_invalid_target(self, diqu: diquRunner) -> None:
    #     invalid_target = "invalid-target"
    #     with pytest.raises(Exception) as e:
    #         diqu.invoke(["run", "--target", invalid_target])
    #         assert str(e) == (f"Could not find adapter target type {invalid_target}!")