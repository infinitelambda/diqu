# Configuration for Snowflake connection

In order to use Snowflake as the data source, we need to get the additional dependencies after installing `diqu`:

```bash
pip install "snowflake-connector-python[pandas]"
pip install "snowflake-connector-python[secure-local-storage]"
```

`diqu` will try to reuse [dbt profile configuration](https://docs.getdbt.com/docs/core/connect-data-platform/snowflake-setup) with supporting 3 authentication methods:

## User / Password authentication

Snowflake can be configured using basic user/password authentication as shown below.

```yaml
# ~/.dbt/profiles.yml
diqu:
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

## Key Pair Authentication

To use key pair authentication, omit a `password` and instead provide a `private_key_path` and, optionally, a `private_key_passphrase` in your target.

Also you have the option to use a `private_key` string instead of a `private_key_path`. The `private_key` string should be in either Base64-encoded DER format, representing the key bytes, or a plain-text PEM format. Refer to [Snowflake documentation](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-connect) for more info on how they generate the key.

```yaml
# ~/.dbt/profiles.yml
diqu:
  target: dev
  outputs:
    dev:
      type: snowflake
      account: [account id]

      # Keypair config
      private_key_path: [path/to/private.key]
      # OR:
      # private_key: [value is Base64-encoded DER format (key bytes), or a plain-text PEM format]
      private_key_passphrase: [passphrase for the private key, if key is encrypted]

      role: [user role]
      database: [database name]
      warehouse: [warehouse name]
      schema: [dbt schema]
```

## SSO Authentication

To use SSO authentication for Snowflake, omit a `password` and instead supply an `authenticator` config to your target. `authenticator` should be 'externalbrowser' for now.

```yaml
# ~/.dbt/profiles.yml
diqu:
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
