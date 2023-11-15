from diqu.alerts.factory import AlertFactory
from diqu.packages.factory import PackageFactory
from diqu.sources.factory import SourceFactory
from diqu.tasks.base import BaseTask
from diqu.utils.meta import ResultCode


class AlertTask(BaseTask):
    """AlertTask class inherited from BaseTask"""

    def __init__(self, **kwargs) -> None:
        """Initilization: Get 3 modules based on the parameters
        1. Package: where to define the Issue query
        2. Source: which DWH connnection to open and to execute the query
        3. Alert: define the alert format, and which channels need to send the alerts
        """
        super().__init__(**kwargs)
        self.alert = AlertFactory(**kwargs)
        if not self.alert.is_empty():
            self.package = PackageFactory(**kwargs)
            self.source = SourceFactory(**kwargs)

    def run(self) -> ResultCode:
        if self.alert.is_empty():
            return ResultCode.SUCCEEDED

        query = self.package.get_query()
        data = self.source.execute(query=query)
        # data.to_csv(".cache/csv__data.csv", index=False)
        return self.alert.run(data=data)
