<!-- markdownlint-disable code-block-style -->
# Quick Start (`diqu`)

This introduction assumes you are already using dbt (and the dq-tools package) in your project, and have the log table ready.

To get started using `diqu`, we'll go over the steps required & explain what possibilities this package creates for you.

## 1. Installation

<div class="termynal" data-termynal data-ty-typeDelay="40" data-ty-lineDelay="700"> <!-- markdownlint-disable no-inline-html -->
    <span data-ty="input">pip install diqu --upgrade</span>
    <span data-ty="progress"></span>
    <span data-ty>Successfully installed diqu</span>
    <a href="#" data-terminal-control="">restart ↻</a>
</div>

📓 _NOTE_: The required Data Warehouse (DWH) module should already be installed if you are using `diqu` in a working dbt project. If not, please perform additional steps to install these DWH modules.

For example, if you're using Snowflake:

```bash
pip install "snowflake-connector-python[pandas]"
pip install "snowflake-connector-python[secure-local-storage]"
```

## 2. Profile setup

We're trying to reuse the dbt `profiles.yml`'s format regardless to whether you use dbt or not in order to configure the DWH connection, in this case, the Snowflake connection.

The content of the file should be like this:

```yaml
diqu_demo:
  outputs:
    dev:
      type: snowflake
      account: <your_value>
      role: <your_value>

      user: <your_value>
      password: <your_value>

      warehouse: <your_value>
      database: <your_value>
      schema: <your_value>
      threads: <your_value>

  target: dev
```

See more details in [here](./config/sources/snowflake.html).

Or, for just the csv file as the connection:

```yaml
diqu_demo:
  outputs:
    dev:
      type: csv
      dir: ./.cache

  target: dev
```

> In this case, we need to download data into `csv__data.csv` file and put it under `.cache` directory. See how the file is schema-ed [here](./config/packages/custom_query.html).

## 3. Usage

Optionally, try to configure the preflight's rules or skip & leave it as default:

```bash
# define the query params:
# - your_issue_deprecation_time_in_day, default to "3"
export ISSUE_DEPRECATED_WINDOW_IN_DAYS=?
# - your_issue_historical_data_update_window_in_days, default to "14"
export ISSUE_UPDATE_WINDOW_IN_DAYS=?

# build dq-tools log table:
dbt run -s dq_tools
```

And then, run the Alerting:

```bash
diqu alert --to slack --to jira
```

Here is the sample logs:

```log
04:33:17  diqu: INFO - Run with diqu==1.0.0 🏃
04:33:19  diqu: INFO - Using dbt project at: /path/to/dbt/project
04:33:19  diqu: INFO - Using dbt profiles.yml at: ~/.dbt
04:33:19  diqu: INFO - Using snowflake connection
04:33:19  diqu: INFO - Looking for the query in: ./query.sql
04:33:23  diqu: INFO - Alerting to: SLACK
04:33:23  diqu: INFO - ✅ Done > Slack
04:33:23  diqu: INFO - Alerting to: JIRA
04:33:23  diqu: INFO - ✅ Done > JIRA
```

Before we can run the Alerting, surely we need to configure the Alert credentials:

### Slack Channel

Use the environment variables to configure the Slack Channel:

```bash
export SLACK_TOKEN=your_token
export SLACK_CHANNEL=your_channel_name
```

Then, go alert:

```bash
diqu alert --to slack
```

### Jira Board

Use the environment variables to configure the JIRA Board:

```bash
export JIRA_SERVER=your_jira_server e.g. https://your_value.atlassian.net/
export JIRA_AUTH_USER=your_service_account e.g. dqt_user@your_value.com
export JIRA_AUTH_PASSWORD=your_service_token e.g. ATATTxxxxx
export JIRA_PROJECT_ID=your_project_id e.g. 106413
export JIRA_ISSUE_TYPE=your_issue_type, default to "Bug"
export JIRA_OPEN_ISSUES_FILTER_BY_SUMMARY=your_issue_filter_on_title, default to "dq-tools"
```

Then, go alert:

```bash
diqu alert --to jira
```

📖 For more details, please jump to the [User Guide](./common.html) page.

## Quick Demo

[![Watch the video](https://cdn.loom.com/sessions/thumbnails/e9bdbae1b455497d9eaf4ca9518b5797-1697091988047-with-play.gif)](https://www.loom.com/embed/8d970dfe333c450f8f6d3859458cac99?sid=7a4a17d8-7b5d-439d-b954-167afddb63d5)