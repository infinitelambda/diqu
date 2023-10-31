from diqu.utils.module import load_module


class PackageFactory:
    """Package factory class"""

    def __init__(self, **kwargs) -> None:
        """Initilization:
        - Load package module
        - Get the configuration
        """
        self.package = load_module(
            name=kwargs.get("package") or "dq_tools", package="diqu.packages"
        )
        self.config = kwargs

    def get_query(self):
        """Return the SQL query of the configured package

        Returns:
            _type_: _description_
        """
        return self.package.get_query(config=self.config)
