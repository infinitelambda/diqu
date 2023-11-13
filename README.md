# diqu [Experimental]

[![PyPI version](https://badge.fury.io/py/diqu.svg)](https://pypi.org/project/diqu/)
![python-cli](https://img.shields.io/badge/CLI-Python-FFCE3E?labelColor=14354C&logo=python&logoColor=white)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache--2.0-yellow.svg)](https://opensource.org/license/apache-2-0/)
[![python](https://img.shields.io/badge/Python-3.9|3.10|3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![codecov](https://codecov.io/gh/infinitelambda/diqu/graph/badge.svg?token=JUO2ASNQEB)](https://codecov.io/gh/infinitelambda/diqu)

CLI companion tool supporting the Alert / Notification for [![dq-tools](https://img.shields.io/badge/dq--tools-hub-FF694B?logo=dbt&logoColor=FF694B)](https://hub.getdbt.com/infinitelambda/dq_tools) and more.

- [diqu \[Experimental\]](#diqu-experimental)
  - [Installation](#installation)
  - [Usage](#usage)
  - [How to Contribute](#how-to-contribute)
  - [About Infinite Lambda](#about-infinite-lambda)

## Installation

```bash
pip install diqu [--upgrade]
```

📓 NOTE: The DWH module should get installed already if you use `diqu` in a dbt project, if not, please perform additional step, for example, to install snowflake module:

```bash
pip install "snowflake-connector-python[pandas]"
pip install "snowflake-connector-python[secure-local-storage]"
```

## Usage

```bash
dbt run -s dq_tools
diqu alert \
  --project-dir /path/to/dbt/project \
  --to slack --to jira
```

<details> <!-- markdownlint-disable no-inline-html -->
  <summary>Sample logs</summary>

  ```log
  04:33:17  diqu: INFO - Run with diqu==1.0.0 🏃
  04:33:19  diqu: INFO - Using dbt project at: /path/to/dbt/project
  04:33:19  diqu: INFO - Using dbt profiles.yml at: ~/.dbt
  04:33:19  diqu: INFO - Using snowflake connection
  04:33:19  diqu: INFO - Looking for the query in: /path/to/site-packages/diqu/packages/include/dq_tools__get_test_results.sql
  04:33:23  diqu: INFO - Alerting to: SLACK
  04:33:23  diqu: INFO - ✅ Done > Slack
  04:33:23  diqu: INFO - Alerting to: JIRA
  04:33:23  diqu: INFO - ✅ Done > JIRA
  ```

</details>

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
  export ISSUE_DEPRECATED_WINDOW_IN_DAYS=your_issue_deprecation_time_in_day, default to "3"
  export ISSUE_UPDATE_WINDOW_IN_DAYS=your_issue_historical_data_update_window_in_days, default to "14"
  diqu alert --to jira
  ```

## How to Contribute

See [CONTRIBUTING.md](./CONTRIBUTING.md)

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
