<!-- markdownlint-disable no-inline-html -->
# Using custom module script

In case you're NOT ready for publishing the adapters (`diqu-{new-adapter}`), or would like to keep yours privately, it's also supported here.

This is a basic guideline to let you do that:

## Understand the module paths

Check out the our supported [modules](./../common.md#modules), and here is our skeleton:

```bash
diqu/
├── diqu/
    ├── alerts/     # Alert module
    ├── packages/   # Package module
    ├── sources/    # Source module
```

Let's say that we want to create an alert custom script, named `your_alert_module.py`.
Now, we must follow the above directory structure and put the script under `(your_repo)/diqu/alerts/` as below:

```bash
your_repo/
├── diqu/
    ├── alerts/
        ├── your_alert_module.py # custom script here
├── your_other_dir/
```

> Follow the same fashion for the `Package` or `Source` module 👍

## Create your module script

Check out the [Build a new adapter](./community_adapter.md#3-build-a-new-adapter) for more details on how to structure your code.

For example: `(your_repo)/diqu/alerts/your_alert_module.py`

```python
from diqu.utils.log import logger
from diqu.utils.meta import ResultCode


def alert(data) -> ResultCode:
    # your implementation here
    # log any necessary messages e.g. logger.info("✅ Done > My Module")
    return ResultCode.SUCCEEDED # return the ResultCode value
```

## Run `diqu` with the custom module script

Run `diqu alert -h` to inspect the usage for using custom:

- Alert via `--to` option ([docs](./../config/alerts/))
- Package via `--package` option ([docs](./../config/packages/))
- Source via `--profile-name` and `--profiles-dir`  ([docs](./../config/sources/))

For example: `(your_repo)/diqu/alerts/your_alert_module.py`

```bash
diqu alert --to your_alert_module
```

**_Happy Customizing 🚀_**
