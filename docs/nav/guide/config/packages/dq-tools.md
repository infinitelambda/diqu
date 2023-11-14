# Configuration for `dq-tools` dbt package

This is the essential steps to start alerting the Incidents based on the test results which are captured by [![dq-tools](https://img.shields.io/badge/dq--tools-hub-FF694B?logo=dbt&logoColor=FF694B)](https://hub.getdbt.com/infinitelambda/dq_tools) package in a [dbt](https://www.getdbt.com/) project.

## 1. Install `dq-tools` package

dbt version required: >=1.6.0

Include the following in your packages.yml file:

```yaml
packages:
  - package: infinitelambda/dq_tools
    version: 1.4.2
```

Run `dbt deps` to install the package.

For more information on using packages in your dbt project, check out the [dbt Documentation](https://docs.getdbt.com/docs/build/packages).

## 2. Configure the log table & the hook

Log table is containing all the test results produced by dbt Jobs, and surely can be configured by specifying the database or/and the schema.
By default, these info will be getting from the dbt `profiles.yml`.

And the hook is to save the test result if any.

In `dbt_project.yml` file:

```yaml
vars:
  dbt_dq_tool_schema: AUDIT

on-run-end:
  - '{{ dq_tools.store_test_results(results) }}'
```

## 3. Build your models

In `dq-tools`, we decide to save/not to save the test results using the `dq_tools_enable_store_test_results` variable.
By default, it is `False`, therefore let's enable it to have data flew in.

```bash
# init the dq-tools' models
dbt run -s dq_tools
# build your dbt models with saving the test results
dbt build --vars '{dq_tools_enable_store_test_results: true}'
```

## 4. Alerting

Check out the modules' configuration for specific env vars setup. Example:

- [JIRA Configuration](https://diqu.iflambda.com/latest/nav/guide/config/alerts/jira.html)
- [SLACK Configuration](https://diqu.iflambda.com/latest/nav/guide/config/alerts/slack.html)

```bash
# prepare the env vars first
...
# run alerting
diqu alert --query-schema AUDIT
```

> `--query-schema` is required here because we previously configured the `dbt_dq_tool_schema` variable

## 5. Supported dq-tools metadata

- Latest & historical tests' statuses, timestamps, row failed counts, row scanned counts and failed rate.
- `deprecated` status for tests that are not executed and recorded in x days.
- Tests labels (dq_issue_type, kpi_category)
