from abc import ABC, abstractclassmethod

from diqu.utils.meta import ResultCode


class BaseTask(ABC):
    """Abstract Task class"""

    def __init__(self, **kwargs) -> None:
        super().__init__()

    @abstractclassmethod
    def run(self) -> ResultCode:
        """Run the task

        Returns:
            ResultCode: Result code
        """
