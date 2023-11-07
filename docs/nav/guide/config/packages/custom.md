# Configuration for Custom query

If you're not using [dq-tools](https://hub.getdbt.com/infinitelambda/dq_tools) package or even not using [dbt](https://www.getdbt.com/), no problem, we're supporting a custom query directly to your data table/view.

The steps are as following:

## 1. Prepare SQL script

Assuming we have a custom script named `incidents.sql` which is located in the current directory.

The script need to provide the expected columns required for each channels, for example, for JIRA, we need:

- Title
- Description
- Label
- ...(to be updated)

Let's build your `SELECT` query:

```sql
-- incident.sql

select  'your_value' as title,
        ...

from    your_table
```

## 2. Alerting

See [JIRA Configuration](https://diqu.iflambda.com/latest/nav/guide/config/alerts/jira.html) for more details, following is a sample command:

```bash
# prepare the env vars here first
...
# run alerting
diqu alert --query-file incident.sql
```
