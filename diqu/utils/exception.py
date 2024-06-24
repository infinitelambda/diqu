import contextlib

import click


@contextlib.contextmanager
def handle_module_errors(module: str, msg: str = ""):
    try:
        yield
    except Exception as e:
        raise click.UsageError(
            f"Module {module} could not be found ({msg}. Details: {str(e)})"
        )


@contextlib.contextmanager
def handle_file_errors(file: str, msg: str = ""):
    try:
        yield
    except Exception as e:
        raise click.FileError(
            f"File {file} could not be read ({msg}. Details: {str(e)})"
        )


@contextlib.contextmanager
def handle_config_errors(config: str, msg: str = ""):
    try:
        yield
    except Exception as e:
        raise click.BadParameter(
            f"{config} is not reachable ({msg}. Details: {str(e)})"
        )
