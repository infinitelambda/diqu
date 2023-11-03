import click
import pytest

from diqu.utils import module


class TestModule:
    def test_load_module_ok(self):
        from diqu.alerts import jira as alert_module

        assert alert_module == module.load_module(name="jira", package="diqu.alerts")

    def test_load_module_failed(self):
        with pytest.raises(click.UsageError):
            module.load_module(name="invalid_module", package="diqu.alerts")
