# Contributing to `diqu`

`diqu` is open-source software. Whether you are a seasoned open-source contributor or a first-time committer, we welcome and encourage you to contribute code, documentation, ideas, or problem statements to this project.

  - [About this document](#about-this-document)
  - [Getting the code](#getting-the-code)
    - [Installing git](#installing-git)
    - [External contributors](#external-contributors)
  - [Setting up an environment](#setting-up-an-environment)
    - [Tools](#tools)
  - [Testing](#testing)
    - [`pytest`](#pytest)
  - [Submitting a Pull Request](#submitting-a-pull-request)

## About this document

There are many ways to contribute to the ongoing development of `diqu`, such as by participating in discussions and issues.

The rest of this document serves as a more granular guide for contributing code changes to `diqu` (this repository). It is not intended as a guide for using `diqu`, and some pieces assume a level of familiarity with Python development with `poetry`. Specific code snippets in this guide assume you are using macOS or Linux and are comfortable with the command line.

- **Branches:** All pull requests from community contributors should target the `main` branch (default). If the change is needed as a patch for a minor version of dbt that has already been released (or is already a release candidate), a maintainer will backport the changes in your PR to the relevant "latest" release branch (`1.0.<latest>`, `1.1.<latest>`, ...). If an issue fix applies to a release branch, that fix should be first committed to the development branch and then to the release branch (rarely release-branch fixes may not apply to `main`).
- **Releases**: Before releasing a new minor version, we prepare a series of beta release candidates to allow users to test the new version in live environments. This is an important quality assurance step, as it exposes the new code to a wide variety of complicated deployments and can surface bugs before the official release. Releases are accessible via `pip`.

## Getting the code

### Installing git

You will need `git` to download and modify the `diqu` source code. On macOS, the best way to download git is to just install [Xcode](https://developer.apple.com/support/xcode/).

### External contributors

You can contribute to `diqu` by forking the `diqu` repository. For a detailed overview on forking, check out the [GitHub docs](https://help.github.com/en/articles/fork-a-repo). In short, you will need to:

1. Fork the `diqu` repository
2. Clone your fork locally
3. Check out a new branch for your proposed changes
4. Push changes to your fork
5. Open a pull request against `infintelambda/diqu` from your forked repository

## Setting up your dev environment
Here are some helpful tools for local development. While this list is tailored for `diqu` development, many of these tools are used commonly across open-source Python projects.

### Tools

We will use `poetry` in `diqu` development and testing.

So first install poetry via pip:

```bash
python3 -m pip install poetry --upgrade
```

Then, start installing the local environment:

```bash
python3 -m poetry install
python3 -m poetry shell
poe git-hooks
pip install -e .
diqu -h
```

## Testing

Once you're able to test manually & your code change is working as expected, it's important to run existing automated tests, as well as add some new ones. These tests will ensure the following:

- Your code changes do not unexpectedly break other established functionality
- Your code changes can handle all known edge cases
- The functionality you're adding will _keep_ working in the future

### `pytest`

Finally, you can also run a specific test or group of tests using [`pytest`](https://docs.pytest.org/en/latest/).
With a virtualenv active and dev dependencies installed, you can do the following:

```bash
poe test
```

Run tests with coverage report:

```bash
poe test-cov
```

> See [pytest usage docs](https://docs.pytest.org/en/6.2.x/usage.html) for an overview of useful command-line options.

## Submitting a Pull Request

Code can be merged into the current development branch `main` by opening a pull request. A `diqu` maintainer will review your PR. They may suggest code revision for style or clarity, or request that you add unit or integration test(s). These are good things! We believe that, with a little bit of help, anyone can contribute high-quality code.

Automated tests run via GitHub Actions. If you're a first-time contributor, all tests (including code checks and unit tests) will require a maintainer to approve.
Changes in the `diqu` repository trigger integration tests against Postgres.
dbt Labs also provides CI environments in which to test changes to other adapters, triggered by PRs in those adapters' repositories, as well as periodic maintenance checks of each adapter in concert with the latest `diqu` code changes.

Once all tests are passed and your PR has been approved, a `diqu` maintainer will merge your changes into the active development branch. And that's it! Happy developing :tada:
