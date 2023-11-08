<!-- markdownlint-disable code-block-style -->
# CLI Reference (diqu)

Run `diqu --help` or `diqu -h` to see the basic guideline for CLI Reference

<div class="termynal" data-termynal data-ty-typeDelay="40" data-ty-lineDelay="700"><!-- markdownlint-disable no-inline-html -->
    <span data-ty="input" data-ty-prompt="$">diqu -h</span>
    <span data-ty>Usage: diqu [OPTIONS] COMMAND [ARGS]...<br />
<br />
 CLI companion tool to support dq-tools package and more<br />
<br />
Options:<br />
--version Show the version and exit.<br />
--help, -h Show this message and exit.<br />
<br />
Commands:<br />
alert Alert the incidents<br />
<br />
 Specify one of these sub-commands and you can find more help from there.
    </span>
</div>

## diqu alert

Alert the incidents to JIRA Board

**Examples:**
=== "CLI (within dbt project)"

    ```bash
    diqu alert
    ```

=== "CLI (outside of dbt project)"

    ```bash
    diqu alert --project-dir /path/to/dbt
    ```

### Send alerts to other channels

=== "Use `--to` option"

    ```bash
    diqu alert --to <your channel module>
    ```

Current supported channels could be found in `(repo)/diqu/alerts/`:

- JIRA: default
- Slack: `diqu alert --to slack`

### Customize the alert's query

=== "Use `--query-dir` and `--query-file` option"

    ```bash
    diqu alert \
      --query-dir /path/to/dir \
      --query-file myquery.sql
    ```

For example, you'd have a query built in `myquery.sql` file which is located at the root of your dbt project dir e.g. `/opt/alert/mydbt/`, your command should look like:

    ```bash
    diqu alert --query-dir /opt/alert/mydbt --query-file myquery.sql
    ```

### Use a specific dbt profile instead of pointing to the dbt project

=== "Use `--profile-name` option"

    ```bash
    diqu alert --profile-name <my_profile>
    ```

For example, the `dbt_project.yml` is as below:

```yaml  
name: 'my_awesome_dbt'
version: '1.0.0'
config-version: 2

profile: 'my_awesome_dbt_profile' # this is the profile name
...
```

And, the `profiles.yml` content is:

```yaml
my_awesome_dbt_profile:
    target: snowflake
    outputs:
    snowflake:
        type: snowflake
        account: "{{ env_var('DBT_SNOWFLAKE_TEST_ACCOUNT') }}"
        user: "{{ env_var('DBT_SNOWFLAKE_TEST_USER') }}"
        password: "{{ env_var('DBT_ENV_SECRET_SNOWFLAKE_TEST_PASSWORD') }}"
        role: "{{ env_var('DBT_SNOWFLAKE_TEST_ROLE') }}"
        database: "{{ env_var('DBT_SNOWFLAKE_TEST_DATABASE') }}"
        warehouse: "{{ env_var('DBT_SNOWFLAKE_TEST_WAREHOUSE') }}"
        schema: "{{ env_var('DBT_SCHEMA') }}"
        threads: 10

my_other_dbt_profile:
    target: snowflake
    ...
```

Finally, the command is: `diqu alert --profile-name my_awesome_dbt_profile` which can be run anywhere (inside or outside of the dbt project dir).

### Configure the SQL context in case that your table/view is on a different schema or database configured in the dbt profile

=== "Use `--query-database` and `--query-schema` option"

    ```bash
    diqu alert --query-database <db> --query-schema <schema>
    ```

Additionally, in the query file [dq_tools__get_test_results.sql](https://github.com/infinitelambda/diqu/blob/main/diqu/packages/include/dq_tools__get_test_results.sql), you need to have a configuration to specify the main table/view which is:
    ```sql
    with

    source as (
      select * from $database.$schema.dq_issue_log
    ),
    ...
    ```

- `--query-database` value will replace `$database` placeholder
- `--query-schema` value will replace `$schema` placeholder
