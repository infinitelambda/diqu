# Configuration for Jira module

This module creates new Jira issues and/or updates current issues based on your input test results.

## Jira Project requirements

Besides basic credentials such as `JIRA_SERVER`, `JIRA_AUTH_USER`, `JIRA_AUTH_PASSWORD` and `JIRA_PROJECT_ID` as specified in the next section, your Jira Project will also need the following:

- A dedicated issue type for our tool, defined by `JIRA_ISSUE_TYPE`, defaults to "Bug" 🐛.
- This issue type must have its `Labels` field [enabled](https://support.atlassian.com/jira-service-management-cloud/docs/add-fields-to-a-screen/).
- Only 1 `Done` status under the `Done` status category. We are using `Done` as a filter for open issues, so something like `Archived` under `Done` category would mess up the update logic.
- A dedicated `JIRA_OPEN_ISSUES_FILTER_BY_SUMMARY`. This is the issue summary suffix to identify issues that we should manage using the module with other issues from the same Jira project. Defaults to "dq-tools"

## Jira module config variables & CLI commands

- `JIRA_SERVER` = your_jira_server (e.g. `https://your_value.atlassian.net/`)
- `JIRA_AUTH_USER` = your_service_account (e.g. `user@your_value.com`)
- `JIRA_AUTH_PASSWORD` = your_service_token (e.g. ATATTxxxxx)
- `JIRA_PROJECT_ID` = your_project_id (e.g. 123456)
- `JIRA_ISSUE_TYPE` = your_issue_type (default to "Bug")
- `JIRA_OPEN_ISSUES_FILTER_BY_SUMMARY` = our_issue_filter_on_title (default to "dq-tools")

All Jira configs are currently environment variables, you can set them up using the sample code below:

```bash
export JIRA_SERVER=https://your_value.atlassian.net/
export JIRA_AUTH_USER=dqt_user@your_value.com
export JIRA_AUTH_PASSWORD=ATATTxxxxx
export JIRA_PROJECT_ID=123456
export JIRA_ISSUE_TYPE=Bug
export JIRA_OPEN_ISSUES_FILTER_BY_SUMMARY=dq-tools
```

To trigger Jira's actions (create and/or update issues), use the following:

```bash
diqu alert --to jira
```

## Issue summary (title)

The issue's summary (aka issue's title) consists of the following parts:
> Status of the latest execution + test_id(hash) + issue filter

Example: `🟡 | Warning in test: accepted_values_my_first_dbt_model_id__False__1__2.ee252c12b8 [dq-tools]`

> Note that dbt singular tests don't have a hash suffix, only test names. Hence, if we change the content of a singular test, their test IDs stay the same and the following statuses will still be updated in the same Jira issue.
> On the other hand, generic test IDs change if we modify their contents, so the module will in turn create a new issue instead.

## The relationship between Jira issue and the DBT test

A Jira issue (aka a Jira ticket - defined by `issue_key`) corresponding to 01 dbt test (defined by `test_id`).

Even though there might be multiple executions of 1 test in our test_results table, all of these executions' metadata are displayed in the same Jira issue if the issue is still in the `open` state (issue' status != `Done`)

In the case where our `test_id` latest status is not `pass`, and the previous corresponding issue has been marked `Done`, the module will **create** a new issue instead of **updating** the previous one.

In short:

- A new issue is created when:
  - Latest test status != `pass`
  - There is no corresponding `issue_key`, or the previous `issue_key` has been marked `Done`
- A current issue is updated when:
  - There is a corresponding `issue_key` that is not marked `Done`

## Automatically mark a Jira Issue as `Done` ✅

Even though it seems very straightforward, we don't automate the process of marking issues as Done as soon as there's a `pass` status.

The reason is the fluctuations in some test results. We have experienced cases where tests passed and failed randomly in each ETL run, which makes the `Done` status for those issues incorrect (our tool might create a new issue in the next run).

Therefore, until there's a unified approach to this problem, marking Done each Jira issue should be done manually after a thorough assessment of previous statuses.

## Test metadata in Jira issue

Below is the list of test metadata displayed in a Jira issue, and the corresponding issue's component [ `Summary`, `Description`, `Labels` ]  that they are in:

- Test metadata:
  - Test ID [ `Summary` & `Description` ]
  - Test tags [ `Labels` ]
- Latest execution metadata [ `Description` ]
  - Latest Status: warn
  - Latest Run Timestamp
  - Latest Run Failed Rate
- Arrays of previous executions' metadata [ `Description` ]
  - Previous statuses
  - Previous run timestamps (UTC)
  - Previous # of failed records
  - Previous # of scanned records

### Issue description sample

A sample issue description is as follows:

>- Test ID: — "MY_FIRST_DBT_MODEL"|id|||test.diqu_dev.accepted_values_my_first_dbt_model_id_False1_2.ee252c12b8 —
>- Latest Status: warn
>- Latest Run Timestamp: 2023-11-14 09:29:42.456000 (UTC)
>- Latest Run Failed Rate: 0.25
>- Previous statuses: ["🟢", "🟢", "🟡", "🟡", "🟡"]
>- Previous run timestamps (UTC): [ "2023-11-07 11:04:10.762", "2023-11-07 10:58:31.607", "2023-11-07 10:52:53.111", "2023-11-07 10:51:24.584", "2023-11-07 10:15:31.166"]
>- Previous # of failed records: [ 1, 1, 1, 1, 1]
>- Previous # of scanned records: [ 4, 4, 4, 4, 4]
>- tag 1: accepted values
>- tag 2: Accuracy
>
> Managed by diqu | modified at 2023-11-14 09:31:58.832864 (UTC)

![Alt text](/assets/img/diqu-alert--jira.png)
