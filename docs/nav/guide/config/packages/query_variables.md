# Configuration for Query Variables

Currently, Query variables are only defined in the query for `dq-tools`. They are not compulsory if you are using CSV as the Source Module, or Custom Query as the Package Module.

However, it is highly recommended to define query variables for flexibility in controlling when & how your alerts would be fired.

For example, with the built-in `dq-tools` Package Module, we are using the following 2 environment variables:

- `ISSUE_DEPRECATED_WINDOW_IN_DAYS` (default = 3 days): Identify when an issue is marked as deprecated by comparing the last executed timestamp of each issue with the current `sysdate()`
- `ISSUE_UPDATE_WINDOW_IN_DAYS` (default = 14 days): Identify the update window to limit the number of rows returned by our query. In other words, in the default case of 14, only the tests that were executed in the last 14 days from the current `sysdate()` are returned.

See [`dq_tools__get_test_results.sql`](https://github.com/infinitelambda/diqu/blob/main/diqu/packages/include/dq_tools__get_test_results.sql) in the code base for details.

To configure these environment variables, use the following:
  ```bash
  export ISSUE_DEPRECATED_WINDOW_IN_DAYS=3
  export ISSUE_UPDATE_WINDOW_IN_DAYS=14
  ```
