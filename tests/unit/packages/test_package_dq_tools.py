from unittest import mock

import pytest

from diqu.packages import dq_tools
from diqu.packages.query import Query


class TestPackageDqTools:
    @pytest.mark.parametrize("config", [(dict()), (dict(query_file="irrelevant.sql"))])
    @mock.patch.object(Query, "take")
    def test_get_query(self, mock_take, config):
        mock_take.return_value = "irrelevant"
        assert "irrelevant" == dq_tools.get_query(config=config)
        assert 1 == mock_take.call_count
        mock_take.assert_called_with(
            config.get("query_file", "dq_tools__get_test_results.sql")
        )
