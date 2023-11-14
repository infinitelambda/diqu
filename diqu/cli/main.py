import rich_click as click

from diqu.cli import common
from diqu.tasks.alert import AlertTask


# diqu
@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
    no_args_is_help=True,
    epilog="Specify one of these sub-commands and you can find more help from there.",
)
@click.version_option(common.VERSION)
@click.pass_context
def diqu(ctx, **kwargs):
    """CLI companion tool to support dq-tools package"""


# diqu alert
@diqu.command(name="alert")
@click.pass_context
@common.options
@common.preflight
def alert(ctx, **kwargs):
    """Alert the issues"""
    exit(AlertTask(**kwargs).run())
