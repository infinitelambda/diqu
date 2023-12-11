<!-- markdownlint-disable code-block-style ul-indent -->
# diqu

[![Documentation](https://img.shields.io/badge/Documentation-Check%20it%20out%20📖-blue?style=flat)](https://diqu.iflambda.com/latest/)
[![PyPI version](https://badge.fury.io/py/diqu.svg)](https://pypi.org/project/diqu/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache--2.0-yellow.svg)](https://opensource.org/license/apache-2-0/)
![python-cli](https://img.shields.io/badge/CLI-Python-FFCE3E?labelColor=14354C&logo=python&logoColor=white)
[![python](https://img.shields.io/badge/Python-3.9|3.10|3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![codecov](https://codecov.io/gh/infinitelambda/diqu/graph/badge.svg?token=JUO2ASNQEB)](https://codecov.io/gh/infinitelambda/diqu)

Automate and streamline the alerting/ notification process for dbt test results using this versatile CLI companion tool. Receive detailed alerts & test metadata seamlessly on various platforms, promoting improved collaboration on dbt project issues 🐞🚀.

## Who is this for

This tool is designed for individuals or teams seeking to automate the management of their dbt project issues (test warnings, errors... etc) outside the dbt environment.

## Features

- Automated alerts and notifications based on recorded dbt test results.
- Built-in support for dq-tools and custom query input.
- Auto-labels `deprecated` tests for quick & easy identification.
- Sends succinct and informative messages to a dedicated Slack channel.
- Creates and updates Jira tickets with the latest tests' metadata.

### Supported Modules

- Sources (DWH connections)
    - Snowflake
    - CSV file
- Package (parsing dbt test results)
    - [![dq-tools](https://img.shields.io/badge/dq--tools-hub-FF694B?logo=dbt&logoColor=FF694B)](https://hub.getdbt.com/infinitelambda/dq_tools)
    - Custom query
- Alert Modules (alert/ notification)
    - Jira
    - Slack

## Concept ⭐

!!! quote "dbt alert rant 🟢 🟡 🔴 ⚫ - by `diqu` OG Contributors"
    _Run errors are red,_

    _Test warnings are yellow,_

    _Where's my bug alert,_

    _And joint bugfix workflow?_

<img src="assets/img/diqu_concept.jpeg" alt="diqu Concept"> <!-- markdownlint-disable no-inline-html -->

We made a cool thing called `diqu` (pronounced 'deekoo'), a CLI tool to make bugfix lives a lil bit easier. Its goal is simple: streamlining collaboration and enhancing agility in our daily (if not hourly) bugfix with dbt.

Let's face it, the dbt result log is not built for alerting or team bugfix collaboration. Firstly, test warnings exist only in dbt's log, there's no way to get alerted on new warnings every day (or worse, every hour, depending on your ETL schedules) unless you open the log. Secondly, scrolling through a thousand-line log with the whole team to decide who gonna do what is, well, not a smart idea. `diqu` solves these by simply shipping all the test warnings/ errors, along with their metadata (e.g. latest failure, previous statuses ...) to other platforms (e.g. Slack, Jira) that support better alerting & collaborations.

`diqu` reads your test results table (provided by dbt packages that parse result log, such as [![dq-tools](https://img.shields.io/badge/dq--tools-hub-FF694B?logo=dbt&logoColor=FF694B)](https://hub.getdbt.com/infinitelambda/dq_tools)), transform it into simple yet insightful bug metadata, and send it to your output of choices. The output platforms are modularized, which enables contributors to improve & add more modules if needed.

## Basic Usage

```bash
diqu alert --to slack --to jira
```

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

📖 For more details, please jump to [the User Guide page](nav/guide/common.md) or the [Quick Start](nav/guide/quick_start.md) page.

## How to Contribute

This Auto Alert (`diqu`) tool is an open-source software. Whether you are a seasoned open-source contributor or a first-time committer, we welcome and encourage you to contribute code, documentation, ideas, or problem statements to this project.

👉 See [CONTRIBUTING guideline](nav/dev/contributing.md) for more details

🌟 And then, kudos to **our beloved Contributors**:

<a href="https://github.com/infinitelambda/diqu/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=infinitelambda/diqu" />
</a>

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
