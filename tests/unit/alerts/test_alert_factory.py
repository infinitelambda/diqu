import logging
from unittest import mock

from diqu.alerts.factory import AlertFactory


class TestAlertFactory:
    def test_is_empty_true(self):
        assert AlertFactory().is_empty()
        assert AlertFactory(to=[]).is_empty()

    def test_is_empty_true_with_warning(self, caplog):
        with caplog.at_level(logging.DEBUG):
            assert AlertFactory(to=["not_exists_channel"]).is_empty()
            assert "Module not_exists_channel could not be found" in caplog.text

    def test_is_empty_false(self):
        assert not AlertFactory(to=["jira"]).is_empty()

    @mock.patch("diqu.alerts.jira.alert")
    def test_run(self, mock_alert, caplog):
        AlertFactory(to=["jira"]).run(data="irrelevant")
        assert "Alerting to channel: JIRA" in caplog.text
        assert 1 == mock_alert.call_count

    @mock.patch("diqu.alerts.jira.alert")
    def test_run_no_channel(self, mock_alert, caplog):
        AlertFactory().run(data="irrelevant")
        assert "Alerting to channel:" not in caplog.text
        assert 0 == mock_alert.call_count
