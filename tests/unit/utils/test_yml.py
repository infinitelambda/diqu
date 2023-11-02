from unittest import mock
from diqu.utils import yml
import pytest
import click


class TestYml:
    def test_load_yml_ok(self):
        with mock.patch(
            "builtins.open",
            mock.mock_open(read_data=str.encode("data", encoding="utf-8"))
        ) as mock_file:
            assert "data" == yml.load(file_path="path/to/irrelevant.yml")
        mock_file.assert_called_with("path/to/irrelevant.yml", "r")
    
    def test_load_yml_failed(self):
        with pytest.raises(click.FileError):
            yml.load(file_path="invalid/path/to/irrelevant.yml")