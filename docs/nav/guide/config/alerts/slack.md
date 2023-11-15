# Configuration for Slack module

This module creates and sends a short report on the latest dbt test results to a specific Slack channel via a Slack bot

## Slack requirements

- A dedicated channel for this module messages
- A dedicated Slack bot in the channel & bot token.
    - [Creating a Slack bot](https://infinitelambda.slack.com/customize/slackbot)
    - [Getting your bot token](https://api.slack.com/authentication/token-types#bot)

## Slack module config variables & CLI commands:

- `SLACK_TOKEN`: your Slack bot token (e.g. xxxx-123456789101-12345678910-XXXXXXXXXXXXXXXXXXXXXXX)
- `SLACK_CHANNEL`: your Slack channel (e.g. your_channel_name)

All Slack configs are currently environment variables, you can set them up using the sample code below:

```bash
export SLACK_TOKEN=xxxx-123456789101-12345678910-XXXXXXXXXXXXXXXXXXXXXXX
export SLACK_CHANNEL=your_channel_name
```

To alert to Slack, use the following:

```bash
diqu alert --to slack
```

## Slack message body
Our default Slack message consists of:

- Thread's header + timestamp
- A quick summary: `errors`, `warnings`, `passes`, and `deprecations` count.
- Top 3 issues:
    - If you have previously defined `Priority` field in your custom Query, these are the 3 issues with the highest priority.
    - If not, it's 🌟random 🌟

## Sample Slack message

>:thread: Summary on 2023-11-10 05:47:42.571000:
>
>- :exclamation: 3 error(s)
>- :eyes: 3 warning(s)
>- :white_check_mark: 2 pass(es)
>- :white_check_mark: 0 deprecation(s)
>
>:point_right: Top 3 Issues:
>
>- [1] :large_yellow_circle: | Warning in test: accepted_values_my_first_dbt_model_id__False__1__2.ee252c12b8 [dq-tools]
>- [2] :large_yellow_circle: | Warning in test: accepted_values_my_first_dbt_model_id__False__1__2.ee252c12b8 [dq-tools]
>- [3] :large_yellow_circle: | Warning in test: accepted_values_my_first_dbt_model_id__False__1__2.ee252c12b8 [dq-tools]
