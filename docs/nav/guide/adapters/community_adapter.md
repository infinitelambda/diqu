# Contribute to adapters

Community adapters are plugins contributed and maintained by members of the diqu community. We welcome and encourage contributions to existing adapters or the creation of new adapters (`diqu-{new-adapter}`). Keep in mind that community maintainers are volunteers, so please be kind, understanding, and offer help where possible!

## Contribute to the existing adapters

Anyone can contribute by testing and writing code. If you're interested, check out the open issues in the plugin's source repository. Use the relevant GitHub repo links below:

- Core (`diqu`): [infinitelambda/diqu](https://github.com/infinitelambda/diqu)
- Email plugin (POC only): [datnguye/diqu-email](https://github.com/datnguye/diqu-email)

**Don't see your adapter**❓ Please help to [open a PR](https://github.com/infinitelambda/diqu/compare) to add your plugin to this documentation.

## Create a new adapter

If you see something missing from the lists above, and you're interested in developing an integration, here are the basic guideline on how an adapter is developed in the Build, test, document, and promote adapters:

### 1. Introduction

Since this package is built with [the modular approach](../common.md), the adapters are essential component of `diqu`.

All projects are not the same:

- [Package] _How do we capture the test result logs or any other similar data?_ We use `dq-tools` but it doesn't enforce everyone to follow the same in order to use `diqu`
- [Source] _Which database are we using in the project? We built Snowflake and CSV connection but you will want it to support Big Query for example_
- [Alert] _Ways to alert the Incidents/Anomalies:_ to JIRA or to Azure DevOps? to Slack or to Email? What should be the content of the alert?

### 2. Prerequisites

It is very important that you have the right skills, and understand the level of difficulty required to make an adapter for your Auto Alert.

**Maintaining your adapter:**

When your adapter becomes more popular, and people start using it, you may quickly become the maintainer of an increasingly popular open source project. With this new role, comes some unexpected responsibilities that not only include code maintenance, but also working with a community of users and contributors. To help people understand what to expect of your project, you should communicate your intentions early and often in your adapter documentation or README. Answer questions like, Is this experimental work that people should use at their own risk? Or is this production-grade code that you're committed to maintaining into the future

**Following `diqu` vesioning and keeping compatibility:**

We're highly recomended to follow [the Semantic Version](https://semver.org/) convention. New major or minor version of `diqu` might have the breaking changes which will be clearly communicating through the Release Notes, it is important to put it on the radar and make the changes accordingly to adapt it to your adapter.

We also encourage that your adapter's version should follow the Core's minor version to avoid any future confusion of usage, for example, `diqu` v1.0.x then your adapter `diqu-email` will version as v1.0.x

### 3. Build a new adapter

This step will walk you through the first creating the necessary adapter classes and functions, and provide some resources to help you validate that your new adapter is working correctly. Make sure you've familiarized yourself with the previous steps in this guide.

In the meantime, we don't have the `cookiecutter` template to help you to quickly generate the project from a scaffold.

Here is the project skeleton for your new adapter, for example, `diqu-new-adapter`:

#### Providing extensions for the `alert` module only

```log
(repo)
  | - diqu
  |  | - alerts
  |  | - alerts/__init__.py
  |  | - alerts/<new_module>.py
  | - diqu/__init__.py
```

In your `alerts/<new_module>.py`:

```python
from diqu.utils.log import logger
from diqu.utils.meta import ResultCode


def alert(data) -> ResultCode:
    # your implementation here
    # log any necessary messages e.g. logger.info("✅ Done > My Module")
    # return the ResultCode value
```

And your diqu command will be: `diqu alert --to <new_module>`

#### Providing extensions for the `package` module only

```log
(repo)
  | - diqu
  |  | - packages
  |  | - packages/__init__.py
  |  | - packages/<new_module>.py
  | - diqu/__init__.py
```

In your `packages/<new_module>.py`:

```python
from diqu.utils.log import logger

def get_query(config: dict) -> str:
    # your implementation here, return the SQL query
```

And your diqu command will be: `diqu alert --package <new_module>`

#### Providing extensions for the `source` module only

```log
(repo)
  | - diqu
  |  | - sources
  |  | - sources/__init__.py
  |  | - sources/<new_module>.py
  | - diqu/__init__.py
```

In your `sources/<new_module>.py`:

```python
from diqu.utils.log import logger
from diqu.sources.base import BaseConnection


def get_connection(config: dict) -> BaseConnection:
    # your implementation here, return the BaseConnection class
```

And your diqu command won't be change, but you should make sure the value of `<new_module>` will be exact-match to the dbt profiles' `type` attribute.

#### 💡 Combinations of above will also doable. And in general, here is the whole project as sample:

```log
(repo)
  | - diqu
  |  | - <module>
  |  | - <module>/__init__.py
  |  | - <module>/<new_module>.py
  | - diqu/__init__.py
  | - tests/
  | - LICENSE
  | - pyproject.toml
  | - CONTRIBUTING.md
  | - README.md
```

In `pyproject.toml` file, the content should be:

```yaml
[tool.poetry]
name = "diqu-<new-adapter>"
version = "0.0.0"
description = "Data Quality CLI for the Auto-Alerts - <New Adapter>"
authors = ["Your Name <your_email@domain.com>"]
readme = "README.md"
license = "<YOUR LICENCE>"
repository = "https://<your-repo-url>"
homepage = "https://<your-website-url>"
keywords = ["packaging", "poetry", "data-quality", "alert", "notification", "collaboration", "agility", "flake8", "markdown", "lint"]
classifiers = [
    "Environment :: Console",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Documentation",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Software Development :: Quality Assurance",
]
packages = [
  {include = "diqu"},
  {include = "README.md"},
]

[tool.poetry.dependencies]
python = ">=3.9,<3.13"
diqu = ">=0.1,<0.2"

[tool.poetry.dev-dependencies]
pre-commit = "^2.17.0"
poethepoet = "^0.16.4"
black = "^23.7.0"
flake8 = "^6.0.0"
isort = "^5.12.0"
autoflake = "^2.0.1"
pytest = "^7.2.0"
pytest-sugar = "^0.9.6"
coverage = {version = "^6.5.0", extras = ["toml"]}

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.isort]
multi_line_output = 3
force_to_top = ["os"]
profile = "black"
skip_gitignore = true

[tool.autoflake]
recursive = true
in-place = true
remove-all-unused-imports = true
ignore-init-module-imports = true
remove-unused-variables = true
ignore-pass-statements = false

[tool.coverage.run]
omit = ["tests/*"]

[tool.poe.tasks]
git-hooks = { shell = "pre-commit install --install-hooks && pre-commit install --hook-type commit-msg" }
format = [
  {cmd = "autoflake ."},
  {cmd = "black ."},
  {cmd = "isort ."},
]
lint = [
  {cmd = "black --check ."},
  {cmd = "isort --check-only ."},
  {cmd = "flake8 ."},
]
test = [
  {cmd = "pytest ."},
]
test-cov = [
  {cmd = "pytest --version"},
  {cmd = "coverage run -m pytest ."},
  {cmd = "coverage report --show-missing"},
  {cmd = "coverage xml"},
]
```

### 4. Test your adapter

- Your adapter should be compatible with diqu coresponding minor version
- You should be familiar with pytest: https://docs.pytest.org/

Let's add your testing under `tests/` directory to ensure your new modules working as expected. We will encourage your testing would cover 100% coverage if possible 🚀.

### 5. Publish the new adapter

Many community members maintain their adapter plugins under open source licenses. If you're interested in doing this, we recommend:

- Hosting on a public git provider (for example, GitHub or Gitlab)
- Publishing to [PyPI](https://pypi.org/)
- Open a PR to this page under [Contribute to the existing adapters](#contribute-to-the-existing-adapters) section

**_Happy Coding 🚀_**
