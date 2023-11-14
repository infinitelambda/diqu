from diqu.utils.log import logger
from diqu.utils.module import load_module


class AlertFactory:
    """Alert Factory class"""

    def __init__(self, **kwargs) -> None:
        """Initialization: Load the alert modules"""
        tos = kwargs.get("to") or []
        self.channels = []
        for to in tos:
            try:
                self.channels.append(load_module(name=to, package="diqu.alerts"))
            except Exception as e:
                logger.warning(str(e))

    def is_empty(self) -> bool:
        """Check if any available channels

        Returns:
            bool: True if there is no channels found
        """
        return len(self.channels) == 0

    def run(self, data):
        """Run the alert to the (multiple) channel(s)

        Args:
            data (DataFrame): Issue data collected
        """
        for c in self.channels:
            logger.info(f"Alerting to: {str(c.__name__).split('.')[-1].upper()}")
            c.alert(data=data)
