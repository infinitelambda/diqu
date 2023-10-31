from importlib import import_module
from types import ModuleType

from diqu.utils import exception


def load_module(name: str, package: str = "diqu") -> ModuleType:
    """Import the module dynamically

    Args:
        name (str): Module name e.g. snowflake, dq_tools, jira

    Raises:
        Exception: Module not found

    Returns:
        ModuleType: Imported module
    """
    with exception.handle_module_errors(name, f"{package}.{name}"):
        return import_module(name=f".{name}", package=package)
