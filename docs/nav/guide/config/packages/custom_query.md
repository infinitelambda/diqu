# Configuration for Custom query

If you're not using [dq-tools](https://hub.getdbt.com/infinitelambda/dq_tools) package or even [dbt](https://www.getdbt.com/), no problem, we're supporting a custom query directly to your data table/view.

The steps are as follows:

## 1. Prepare SQL script

Assuming we have a custom script named `issues.sql` which is located in the current directory.

The script has to provide the expected columns required for all modules below:

| Field                        | Description                                                                                          |
|------------------------------|------------------------------------------------------------------------------------------------------|
| `test_id`                    | The unique identifier of the test.                                                                   |
| `test_status`                | Status of the test: 'pass', 'warn', 'fail', 'deprecate'. Example: `accepted_values_my_first_dbt_model_id__False__1__2.ee252c12b8`                                    |
| `test_title`                 | Test's title to be shown in your module (e.g. in the Jira module, `test_title` is used as the issue's summary: `🟡 | Warning in test: test_id [dq-tools]`).    |
| `check_timestamp`            | Test execution timestamp.                                                                            |
| `no_of_records_scanned`      | Number of rows scanned.                                                                              |
| `no_of_records_failed`       | Number of rows that did not pass the test.                                                           |
| `failed_rate`                | Percentage of `no_of_records_failed / nullif(no_of_records_scanned, 0) as failed_rate`.              |
| `tag_1`                      | Your 1st test tag (e.g. 'accepted_value').                                                           |
| `tag_2`                      | Your 2nd test tag (e.g. `Accuracy`).                                                                 |
| `prev_statuses`              | An array of previous statuses (e.g `array_agg(test_status_emoji) within group (order by check_timestamp desc) as prev_statuses`).                          |
| `prev_check_timestamps`      | An array of previous execution times of this test (e.g `array_agg(check_timestamp) within group (order by check_timestamp desc) as prev_check_timestamps`).|
| `prev_no_of_records_scanned` | An array of previous row scanned (e.g `array_agg(no_of_records_scanned) within group (order by check_timestamp desc) as prev_no_of_records_scanned`).  |
| `prev_no_of_records_failed`  | An array of previous row failed (e.g `array_agg(no_of_records_failed) within group (order by check_timestamp desc) as prev_no_of_records_failed`).    |
| `priority`                   | Your priority level for each test. This field will be used for ordering the issues list in all modules. It is recommended to use numbers to simplify the process.        |

Let's build your `SELECT` query:

```sql
-- issue.sql

select  'your_value' as test_id,
        'your_value' as test_status,
        'your_value' as test_title,
        'your_value' as check_timestamp,
        'your_value' as no_of_records_scanned,
        'your_value' as no_of_records_failed,
        'your_value' as failed_rate,
        'your_value' as tag_1,
        'your_value' as tag_2,
        'your_value' as prev_statuses,
        'your_value' as prev_check_timestamps,
        'your_value' as prev_no_of_records_scanned,
        'your_value' as prev_no_of_records_failed,
        'your_value' as priority,

from    your_table
```

## 2. Alerting

### Setting up env vars

Set up Query variables: [Query Variables Config](./query_variables.md)

Set up Alert Module variables:

- [JIRA Configuration](../alerts/jira.md)
- [SLACK Configuration](../alerts/slack.md)

### Executing alert actions

```bash
# prepare the env vars first
...
# run alerting
diqu alert --query-file issue.sql
```
