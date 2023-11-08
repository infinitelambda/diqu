# Configuration for Other connection via CSV file

Currently, the only supported connection is Snowflake, we'll see more added in the near further.

In the meantime, using CSV file is a good option alternatively.

## 1. Configure the dbt profile

Let's create a new target for CSV in dbt `profiles.yml` file:

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

No matter what CLI tool you use to query and download data into csv file which located in `.cache` folder.

The default file name is `csv__data.csv`.

And, the file must contain the following columns:

- title
- ...(to be updated)

## 3. Alerting

```bash
diqu alert --query-dir ./.cache --query_file csv__data.csv --target dev
```
