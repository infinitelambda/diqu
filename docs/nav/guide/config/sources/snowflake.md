# Configuration for Snowflake connection

In order to use Snowflake as the data source, we need to get the additional dependencies after installing `diqu`:

```bash
pip install "snowflake-connector-python[pandas]"
pip install "snowflake-connector-python[secure-local-storage]"
```

`diqu` will try to reuse [dbt profile configuration](https://docs.getdbt.com/docs/core/connect-data-platform/snowflake-setup) with supporting 2 authentication methods:

## User / Password authentication

```yml
# ~/.dbt/profiles.yml
my-snowflake-db:
  target: dev
  outputs:
    dev:
      type: snowflake
      account: [account id]

      # User/password auth
      user: [username]
      password: [password]

      role: [user role]
      database: [database name]
      warehouse: [warehouse name]
      schema: [dbt schema]
```

## SSO Authentication

```yml
# ~/.dbt/profiles.yml
my-snowflake-db:
  target: dev
  outputs:
    dev:
      type: snowflake
      account: [account id]

      # User
      user: [username]
      # SSO config
      authenticator: externalbrowser

      role: [user role]
      database: [database name]
      warehouse: [warehouse name]
      schema: [dbt schema]
```

