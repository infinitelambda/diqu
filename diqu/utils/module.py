import sys
from importlib import import_module, util
from types import ModuleType

from diqu.utils import exception
from diqu.utils.log import logger


def load_module(name: str, package: str = "diqu") -> ModuleType:
    """Import the module dynamically

    Args:
        name (str): Module name e.g. snowflake, dq_tools, jira

    Raises:
        Exception: Module not found

    Returns:
        ModuleType: Imported module
    """
    module_name = f"{package}.{name}"
    with exception.handle_module_errors(name, module_name):
        try:
            mod = import_module(name=f".{name}", package=package)
        except Exception:
            mod = None
            logger.debug(f"Import {module_name} module failed, trying local path...")

        if not mod:
            spec = util.spec_from_file_location(
                module_name, f"{package.replace('.', '/')}/{name}.py"
            )
            mod = util.module_from_spec(spec)
            sys.modules[module_name] = mod
            spec.loader.exec_module(mod)

    return mod
