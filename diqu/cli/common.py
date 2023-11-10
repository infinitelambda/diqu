import os
import functools
import importlib.metadata
from pathlib import Path

import rich_click as click

from diqu.utils.log import logger
from diqu.utils.tracking import track_run

VERSION = importlib.metadata.version("diqu")


def options(func):
    @click.option(
        "--to",
        help="Specify the channel(s) of Alerts. Multiple options.",
        default=["jira"],
        multiple=True,
        show_default=True,
        type=click.STRING,
    )
    @click.option(
        "--package",
        help="Configure the package which defines the SQL query.",
        default="dq_tools",
        show_default=True,
        type=click.STRING,
    )
    @click.option(
        "--target",
        "-t",
        help=(
            "Specify dbt target name." "[default: the default target in profiles.yml]"
        ),
        default=None,
        type=click.STRING,
    )
    @click.option(
        "--project-dir",
        help="Specify dbt project dir.",
        default=Path.cwd(),
        show_default=True,
        type=click.STRING,
    )
    @click.option(
        "--profile-name",
        help=(
            "Specify dbt profile name in dbt_projects.yml file "
            "which will ignore the `--project-dir` value and corresponding parsing stuff"
        ),
        default=None,
        show_default=True,
        type=click.STRING,
    )
    @click.option(
        "--profiles-dir",
        help="Specify dbt profiles.yml's dir.",
        default=Path.home() / ".dbt",
        show_default=True,
        type=click.STRING,
    )
    @click.option(
        "--query-dir",
        help="Specify query's directory which is used to scan the query files.",
        default=os.path.abspath(
            f"{os.path.dirname(os.path.realpath(__file__))}/../packages/include"
        ),
        show_default=True,
        type=click.STRING,
    )
    @click.option(
        "--query-file",
        help=(
            "Specify query file name which contains the query or data. "
            "Default value is vary based on the package module"
        ),
        default=None,
        show_default=True,
        type=click.STRING,
    )
    @click.option(
        "--query-database",
        help=(
            "Use it when configuring the '$database' in the query. "
            "Assuming the current connection database context if not configured."
        ),
        default=None,
        show_default=True,
        type=click.STRING,
    )
    @click.option(
        "--query-schema",
        help=(
            "Use it when configuring the '$schema' in the query. "
            "Assuming the current connection schema context if not configured."
        ),
        default=None,
        show_default=True,
        type=click.STRING,
    )
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)  # pragma: no cover

    return wrapper


def preflight(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Run with diqu=={VERSION} 🏃")

        # Get Context
        ctx = click.get_current_context()

        # Tracking
        ctx.with_resource(
            track_run(run_command=ctx.command.name, params=ctx.params, version=VERSION)
        )

        return func(*args, **kwargs)  # pragma: no cover

    return wrapper
