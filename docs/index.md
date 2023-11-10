<!-- markdownlint-disable code-block-style -->
# diqu

[![PyPI version](https://badge.fury.io/py/diqu.svg)](https://pypi.org/project/diqu/)
![python-cli](https://img.shields.io/badge/CLI-Python-FFCE3E?labelColor=14354C&logo=python&logoColor=white)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache--2.0-yellow.svg)](https://opensource.org/license/apache-2-0/)
[![python](https://img.shields.io/badge/Python-3.9|3.10|3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![codecov](https://codecov.io/gh/infinitelambda/diqu/graph/badge.svg?token=JUO2ASNQEB)](https://codecov.io/gh/infinitelambda/diqu)

CLI companion tool supporting the Alert / Notification for [![dq-tools](https://img.shields.io/badge/dq--tools-hub-FF694B?logo=dbt&logoColor=FF694B)](https://hub.getdbt.com/infinitelambda/dq_tools) and more.

## Installation

<div class="termynal" data-termynal data-ty-typeDelay="40" data-ty-lineDelay="700"> <!-- markdownlint-disable no-inline-html -->
    <span data-ty="input">pip install diqu --upgrade</span>
    <span data-ty="progress"></span>
    <span data-ty>Successfully installed diqu</span>
    <a href="#" data-terminal-control="">restart ↻</a>
</div>

📓 _NOTE_: The DWH module should get installed already if you use `diqu` in a dbt project, if not, please perform additional step, for example, to install snowflake module:

```bash
pip install "snowflake-connector-python[pandas]"
pip install "snowflake-connector-python[secure-local-storage]"
```

## Concept

!!! quote "Alert Romance 🔴 🟡 ⚫ ✅"
    _In the realm where circuits hum and wires entwine,_

    _A bug’s life, oh, how it’s truly divine._

    _In the world of engineering, where chaos thrives,_

    _Auto Alert, our savior, arrives._

<img src="assets/img/diqu_concept.jpeg" alt="diqu Concept" width="600"> <!-- markdownlint-disable no-inline-html -->

In the efforts of making our bug's life easier, `diqu` CLI is born with a significant impact, streamlining collaboration and enhancing agility in our daily tasks. This tool takes charge of handling the beloved "chick" of our engineering world: **Anomalies** or **Incidents** 🐞

Alongside our methods for detecting these anomalies in our data, it's important to ensure the Auto Alert trigger is firmly in place, ready to notify us promptly. Together, these innovations pave the way for a more efficient and seamless bug-fighting experience 🚀

## Usage

```bash
dbt run -s dq_tools # optional
diqu alert --to jira
```

<details> <!-- markdownlint-disable no-inline-html -->
  <summary>Sample logs</summary>

  ```log
  04:33:17  diqu: INFO - Run with diqu==1.0.0 🏃
  04:33:19  diqu: INFO - Using dbt project at: /path/to/dbt/project
  04:33:19  diqu: INFO - Using dbt profiles.yml at: ~/.dbt
  04:33:19  diqu: INFO - Using snowflake connection
  04:33:19  diqu: INFO - Looking for the query in: /path/to/file.sql
  04:33:23  diqu: INFO - Alerting to module: JIRA
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
  export JIRA_INCIDENT_ISSUE_TYPE=your_issue_type, default to "[System] Incident"
  export JIRA_OPEN_ISSUES_FILTER=your_issue_filter_on_title, default to "*dq_tools"
  diqu alert --to jira
  ```

## How to Contribute

👉 See [CONTRIBUTING.md](./nav/dev/contributing.html)

## About Infinite Lambda

Infinite Lambda is a cloud and data consultancy. We build strategies, help organisations implement them and pass on the expertise to look after the infrastructure.

We are an Elite Snowflake Partner, a Platinum dbt Partner and two-times Fivetran Innovation Partner of the Year for EMEA.

Naturally, we love exploring innovative solutions and sharing knowledge, so go ahead and:

🔧 Take a look around our [Git](https://github.com/infinitelambda)

✏️ Browse our [tech blog](https://infinitelambda.com/category/tech-blog/)

We are also chatty, so:

👀 Follow us on [LinkedIn](https://www.linkedin.com/company/infinite-lambda/)

👋🏼 Or just [get in touch](https://infinitelambda.com/contacts/)

[<img src="https://raw.githubusercontent.com/infinitelambda/cdn/1.0.0/general/images/GitHub-About-Section-1080x1080.png" alt="About IL" width="500">](https://infinitelambda.com/)
