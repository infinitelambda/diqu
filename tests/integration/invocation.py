from typing import List
import click

from diqu.cli.main import diqu
from diqu.utils.meta import ResultCode


class diquRunner:
    """Programatic Invocation"""

    def __init__(self) -> None:
        pass

    def invoke(self, args: List[str]):
        """Invoke a command of diqu programatically

        Args:
            args (List[str]): diqu arguments

        Raises:
            Exception: Unhandled exception
            Exception: Not Supported command exception
        """
        try:
            diqu_ctx = diqu.make_context(diqu.name, args)
            return diqu.invoke(diqu_ctx)
        except click.exceptions.Exit as e:
            # 0 exit code, expected for --version early exit
            if str(e) == "0":
                return [], True
            raise Exception(f"unhandled exit code {str(e)}")
        except (click.NoSuchOption, click.UsageError) as e:
            raise Exception(e.message)
