# Configuration for Jira module

- 'deprecate' status is an imediate label and won't be shown in Previous statuses
- Do not change the Test ID: —-- **** --- in description
- tag 1 & tag 2 = Jira lable, in dq_tool it's KPI category & dq lables
- How each issue is constructed:
    - Summary = Status + test id + hash if applicable
        - Singular test doesnt have hash, and will be recognize as the same test even if the content changes, as long as the name stay the same. This doesn't apply for generic test as the hash/ name change.
    - Description (TEST ID for mapping)
    - Label
- Note on fluctuating tests
- Test that has passed since the previous warn or error WONT BE MARKED DONE
