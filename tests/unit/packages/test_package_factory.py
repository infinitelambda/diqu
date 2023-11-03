from unittest import mock

import click
import pytest

from diqu.packages import dq_tools
from diqu.packages.factory import PackageFactory


class TestPackageFactory:
    def test_failed_to_init(self):
        with pytest.raises(click.UsageError):
            PackageFactory(package="irrelevant")

    @mock.patch("diqu.packages.dq_tools.get_query")
    @mock.patch("diqu.packages.factory.load_module")
    def test_get_query(self, mock_load_module, mock_get_query):
        mock_load_module.return_value = dq_tools
        mock_get_query.return_value = "irrelevant"
        actual = PackageFactory().get_query()
        assert actual == "irrelevant"
        assert 1 == mock_load_module.call_count
        assert 1 == mock_get_query.call_count
