import os
from unittest import mock

import pytest

from diqu.sources.base import BaseConnection


class DummyConnection(BaseConnection):
    def __init__(self, **config) -> None:
        super().__init__(**config)

    def execute(self, query: str):
        return None


class DummyConnectionEnvVar(BaseConnection):
    def __init__(self, **config) -> None:
        super().__init__(**config)

    def execute(self, query: str):
        return None


class TestSourceBase:
    @pytest.mark.parametrize(
        "config, attr, result",
        [
            (dict(attr1="attr1_value"), "attr1", "attr1_value"),
            (dict(attr1="attr1_value"), "irrelevant", None),
        ],
    )
    def test_get_profile_config(self, config, attr, result):
        assert result == DummyConnection(**config).get_profile_config(attr=attr)
        DummyConnection.clear()

    @pytest.mark.parametrize(
        "config, attr, attr_env_value, result",
        [
            (
                dict(attr1="env_var('ATTR_ENV_INVALID')"),
                "attr1",
                "attr1_env_value",
                None,
            ),
        ],
    )
    def test_get_profile_config_with_wrong_env_vars(
        self, config, attr, attr_env_value, result
    ):
        with mock.patch.dict(os.environ, {"ATTR1_ENV": attr_env_value}):
            assert result == DummyConnectionEnvVar(**config).get_profile_config(
                attr=attr
            )
            DummyConnectionEnvVar.clear()
