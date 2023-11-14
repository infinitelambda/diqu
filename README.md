# diqu

[![Documentation](https://img.shields.io/badge/Documentation-Check%20it%20out%20📖-blue?style=flat)](https://diqu.iflambda.com/latest/)
[![PyPI version](https://badge.fury.io/py/diqu.svg)](https://pypi.org/project/diqu/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache--2.0-yellow.svg)](https://opensource.org/license/apache-2-0/)
![python-cli](https://img.shields.io/badge/CLI-Python-FFCE3E?labelColor=14354C&logo=python&logoColor=white)
[![python](https://img.shields.io/badge/Python-3.9|3.10|3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![codecov](https://codecov.io/gh/infinitelambda/diqu/graph/badge.svg?token=JUO2ASNQEB)](https://codecov.io/gh/infinitelambda/diqu)

CLI Companion Tool with built-in Alert / Notification features for [![dq-tools](https://img.shields.io/badge/dq--tools-hub-FF694B?logo=dbt&logoColor=FF694B)](https://hub.getdbt.com/infinitelambda/dq_tools) and maybe more with empowering bug management with streamlined collaboration, agility, and automated anomaly alerts for a more efficient bug-fighting experience 🐞🚀.

> 🔴 🟡 ⚫ ✅ </br>
>_In the realm where circuits hum and wires entwine,_</br>
>_A bug’s life, oh, how it’s truly divine._</br>
>_In the world of engineering, where chaos thrives,_</br>
>_Auto Alert, our savior, arrives._

<img src="./docs/assets/img/diqu_concept.jpeg" alt="diqu Concept"> <!-- markdownlint-disable no-inline-html -->

## Installation

```bash
pip install diqu [--upgrade]
```

📓 The DWH module should be available already if you use `diqu` CLI in a `dbt` project, if not, please perform additional installation, for example, snowflake module:

```bash
pip install "snowflake-connector-python[pandas]"
pip install "snowflake-connector-python[secure-local-storage]"
```

## Usage

<details> <!-- markdownlint-disable no-inline-html -->
  <summary>preflight</summary>

  ```bash
  # define the query params
  export ISSUE_DEPRECATED_WINDOW_IN_DAYS=your_issue_deprecation_time_in_day, default to "3"
  export ISSUE_UPDATE_WINDOW_IN_DAYS=your_issue_historical_data_update_window_in_days, default to "14"

  # build dq-tools log table
  dbt run -s dq_tools
  ```

</details>

```bash
diqu alert --to slack --to jira
```

```log
04:33:17  diqu: INFO - Run with diqu==1.0.0 🏃
04:33:19  diqu: INFO - Using dbt project at: /path/to/dbt/project
04:33:19  diqu: INFO - Using dbt profiles.yml at: ~/.dbt
04:33:19  diqu: INFO - Using snowflake connection
04:33:19  diqu: INFO - Looking for the query in: ./dq_tools__get_test_results.sql
04:33:23  diqu: INFO - Alerting to: SLACK
04:33:23  diqu: INFO - ✅ Done > Slack
04:33:23  diqu: INFO - Alerting to: JIRA
04:33:23  diqu: INFO - ✅ Done > JIRA
```

In particular to the alert module, here are the additional configurations:

- For SLACK, you need to use the environment variables to configure the Slack Channel:

  ```bash
  export SLACK_TOKEN=your_token
  export SLACK_CHANNEL=your_channel_name
  diqu alert --to slack
  ```

- For JIRA, you need to use the environment variables to configure the JIRA Board:

  ```bash
  export JIRA_SERVER=your_jira_server e.g. https://your_value.atlassian.net/
  export JIRA_AUTH_USER=your_service_account e.g. dqt_user@your_value.com
  export JIRA_AUTH_PASSWORD=your_service_token e.g. ATATTxxxxx
  export JIRA_PROJECT_ID=your_project_id e.g. 106413
  export JIRA_ISSUE_TYPE=your_issue_type, default to "Bug"
  export JIRA_OPEN_ISSUES_FILTER_BY_SUMMARY=your_issue_filter_on_title, default to "dq-tools"
  diqu alert --to jira
  ```

> For more details, please help to visit [the documentation site](https://diqu.iflambda.com/latest/).

## How to Contribute

This (`diqu`) tool is an open source software. Whether you are a seasoned open source contributor or a first-time committer, we welcome and encourage you to contribute code, documentation, ideas, or problem statements to this project.

👉 See [CONTRIBUTING guideline](./nav/dev/contributing.html) for more details, or alternatively check [CONTRIBUTING.md](./CONTRIBUTING.md)

👉 And then, super thanks to **our beloved Contributors**:

<a href="https://github.com/infinitelambda/diqu/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=infinitelambda/diqu" />
</a>

## About Infinite Lambda

Infinite Lambda is a cloud and data consultancy. We build strategies, help organisations implement them and pass on the expertise to look after the infrastructure.

We are an Elite Snowflake Partner, a Platinum dbt Partner and two-times Fivetran Innovation Partner of the Year for EMEA.

Naturally, we love exploring innovative solutions and sharing knowledge, so go ahead and:

🔧 Take a look around our [Git](https://github.com/infinitelambda) </br>
✏️ Browse our [tech blog](https://infinitelambda.com/category/tech-blog/)

We are also chatty, so:</br>
#️⃣ Follow us on [LinkedIn](https://www.linkedin.com/company/infinite-lambda/) </br>
👋🏼 Or just [get in touch](https://infinitelambda.com/contacts/)

[<img src="https://raw.githubusercontent.com/infinitelambda/cdn/1.0.0/general/images/GitHub-About-Section-1080x1080.png" alt="About IL" width="500">](https://infinitelambda.com/)
