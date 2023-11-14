# User Guide

## Modules
`diqu` CLI is built in the modular approach with 3 main ones:

1. **Source Modules**: Build **_Data Source connections_** (e.g. [Snowflake](./config/sources/snowflake.html), [csv file](./config/sources/custom_csv.html))
2. **Package Modules**: Manage the **_Query_** of the issues captured (e.g. `dq-tools`'s [query](./config/packages/dq-tools.html))
3. **Alert Modules**: Define how to **_alert/notify_** the issue **_to which platforms_** (e.g. [Jira](./config/alerts/jira.html), [Slack](./config/alerts/slack.html))

👉 _See the next pages for more information on how to configure the modules_

## How it works
Generally, `diqu` executes the following steps:

1. Takes in dbt test results from your **Source Module** of choice, let refer to this as the `test_results` table.
    - Depending on the **Package Module** you are using, the schema of this table might vary.
    - If you are using CSV as the Source Module, the schema of `test_results` should be defined by the `.csv`.

2. A Query specified for this `test_results`'s schema is executed to produce the common `test metadata` for **Alert Module**
3. The **Alert Module** of choice takes the `test metadata` in the previous steps and sends it to the specified destinations

## Issue Statuses & Issue Deprecation

Besides the basic dbt test statuses (`pass`, `warn`, `error`), in the built-in query for `dq-tools`, we introduced the new status of `deprecate`.

`deprecate` means no longer valid, and we don't need to take immediate action.

A test is marked `deprecate` if it's not executed & recorded in a specified number of days.

This can defined by the `ISSUE_DEPRECATED_WINDOW_IN_DAYS` variable (see [Query Variables Config](./config/packages/query_variables.html))

Our built-in query also labels each status with its corresponding "traffic lights" icon for easier identification.

- `pass`(🟢)
- `warn`(🟡)
- `failed`(🔴)
- `deprecate`(⚫)

>The statuses of each executed dbt test are crucial for issue management, hence **it is highly recommended to include in your custom CSV or custom Query** if you're building one yourself.
