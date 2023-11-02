from unittest import mock

from diqu.alerts.factory import AlertFactory
from diqu.packages.factory import PackageFactory
from diqu.sources.factory import SourceFactory
from diqu.tasks.alert import AlertTask
from diqu.utils.meta import ResultCode


class TestAlertTask:
    @mock.patch.object(SourceFactory, "execute")
    @mock.patch.object(PackageFactory, "get_query")
    @mock.patch.object(AlertFactory, "is_empty")
    def test_run_with_no_alert_channels(
        self, mock_is_empty, mock_get_query, mock_execute
    ):
        mock_is_empty.return_value = True
        assert ResultCode.SUCCEEDED == AlertTask(**dict(to=[])).run()
        assert 2 == mock_is_empty.call_count
        assert 0 == mock_get_query.call_count
        assert 0 == mock_execute.call_count

    @mock.patch.object(SourceFactory, "__init__")
    @mock.patch.object(PackageFactory, "__init__")
    @mock.patch.object(AlertFactory, "__init__")
    @mock.patch.object(SourceFactory, "execute")
    @mock.patch.object(PackageFactory, "get_query")
    @mock.patch.object(AlertFactory, "run")
    @mock.patch.object(AlertFactory, "is_empty")
    def test_run_with_channels(
        self,
        mock_is_empty,
        mock_run,
        mock_get_query,
        mock_execute,
        mock_alert_init,
        mock_package_init,
        mock_source_init,
    ):
        rr = 1
        mock_alert_init.return_value = None
        mock_package_init.return_value = None
        mock_source_init.return_value = None
        mock_is_empty.return_value = False
        mock_run.return_value = rr
        mock_get_query.return_value = "irrelevant"
        mock_execute.return_value = "irrelevant"
        assert rr == AlertTask().run()
        assert 2 == mock_is_empty.call_count
        assert 1 == mock_run.call_count
        assert 1 == mock_get_query.call_count
        assert 1 == mock_execute.call_count
