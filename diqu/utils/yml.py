import yaml

from diqu.utils import exception


def load(file_path: str):
    """Load YAML file content

    Args:
        file_path (str): YAML file path

    Raises:
        click.FileError: Read file error

    Returns:
        dict: yaml content
    """
    with exception.handle_file_errors(file_path):
        with open(file_path, "r") as stream:
            return yaml.safe_load(stream)
