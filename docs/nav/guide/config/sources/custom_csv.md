# Configuration for Other connection via CSV file

Currently, the only supported connection is Snowflake, we'll see more added in the near future.

In the meantime, using a CSV file is a good alternative.

## 1. Configure the dbt profile

Let's create a new target for CSV in the dbt `profiles.yml` file:

```yaml
ci:
  target: dev
  outputs:
    dev:
      type: csv
      dir: ./.cache
      # dir: "{{ env_var('DQT_CSV_DIR') }}"
```

## 2. Generate CSV file

No matter what CLI tool you use, it is required to query and save data into a `.csv` file in `.cache` folder.

The default file name is `csv__data.csv`.

The file's schema **must be** defined with the same column names as specified in [Custom Query Config](../packages/custom_query.md)

## 3. Alerting

```bash
diqu alert --target dev \
  --query-dir ./.cache --query_file csv__data.csv
  --package csv
```
