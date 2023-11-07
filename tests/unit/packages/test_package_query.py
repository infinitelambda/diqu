from pathlib import Path
from unittest import mock

import pytest

from diqu.packages.query import Query


class TestPackageQuery:
    def test_default_dir(self):
        query = Query()
        assert query.dir == str((Path.cwd() / "diqu/packages/include").absolute())

    @pytest.mark.parametrize(
        "sql_in, sql_out, query_schema, query_database",
        [
            ("data_1", "data_1", None, None),
            ("data_2", "data_2", None, None),
            (
                "select * from $schema.table",
                "select * from schema_1.table",
                "schema_1",
                None,
            ),
            ("select * from $schema.table", "select * from table", None, None),
            (
                "select * from $database.$schema.table",
                "select * from database_1.schema_1.table",
                "schema_1",
                "database_1",
            ),
            (
                "select * from $database.$schema.table",
                "select * from schema_1.table",
                "schema_1",
                None,
            ),
            (
                "select * from $database.$schema.table",
                "select * from table",
                None,
                None,
            ),
            (
                "select * from $database.$schema.table",
                "select * from database_1.table",  # invalid case but valid flow
                None,
                "database_1",
            ),
        ],
    )
    def test_take_ok(self, sql_in, sql_out, query_schema, query_database, caplog):
        with mock.patch(
            "builtins.open",
            mock.mock_open(read_data=sql_in),
        ) as mock_file:
            actual = Query(
                query_dir="irrelevant",
                query_schema=query_schema,
                query_database=query_database,
            ).take(file="irrelevant.sql")
            assert sql_out == actual
        mock_file.assert_called_with("irrelevant/irrelevant.sql", "r")
        assert "Looking for the query in: irrelevant/irrelevant.sql" in caplog.text
