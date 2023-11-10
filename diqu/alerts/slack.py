import os
import ssl
import string
import uuid

import certifi
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from diqu.utils.log import logger
from diqu.utils.meta import ResultCode


def alert(data, limit: int = 3) -> ResultCode:
    """Slack Alert

    Args:
        data (_type_): DataFrame of test results
        limit (int, optional): Limit the top incidents in details of the alert. Defaults to 3.

    Returns:
        ResultCode: Result code
    """
    template_sum = string.Template(
        "🧵 *Summary on $date:*\n\n"
        "  • 🔴 $error_count error(s)\n"
        "  • 🟡 $warn_count warning(s)\n"
        "  • 🟢 $pass_count pass(es)\n"
        "  • ⚫ $deperecated_count deprecation(s)"
    )
    template_incident = string.Template("[$index] $incident\n")
    summary = (
        template_sum.substitute(
            date=data["CHECK_TIMESTAMP"].iloc[0],
            error_count=data[data["TEST_STATUS"] == "failed"].shape[0],
            warn_count=data[data["TEST_STATUS"] == "warn"].shape[0],
            pass_count=data[data["TEST_STATUS"] == "pass"].shape[0],
            deperecated_count=data[data["TEST_STATUS"] == "deprecated"].shape[0],
        )
        if not data.empty
        else "(No Data)"
    )

    incident_data = (
        data[(data["TEST_STATUS"] != "pass") & (data["TEST_STATUS"] != "deprecated")]
        .sort_values("PRIORITY", ascending=True)
        .head(limit)
    )
    if incident_data.empty:
        logger.info("✅ Empty Data | No Alert required > Slack")
        return ResultCode.SUCCEEDED

    incidents = ""
    for i in range(len(incident_data)):
        incidents += template_incident.substitute(
            index=i + 1,
            incident=incident_data.iloc[i, 0],  # first column: TEST_TITLE
        )

    r = Slack().post_message(
        blocks=[
            {"type": "section", "text": {"type": "mrkdwn", "text": summary}},
            {"type": "divider"},
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"👉 *Top {limit} Issues*:\n\n{incidents or '(No Data)'}",
                },
            },
        ]
    )
    if r == ResultCode.SUCCEEDED:
        logger.info("✅ Done > Slack")

    return r


class Slack:
    """Slack Alert class"""

    def __init__(self) -> None:
        """Initialization"""
        self.client = WebClient(
            token=os.environ.get("SLACK_TOKEN"),
            ssl=ssl.create_default_context(cafile=certifi.where()),
        )
        self.channel = os.environ.get("SLACK_CHANNEL")
        self.channel_id = self.find_channel_id(self.channel)

    def post_message(self, text=None, blocks=[]) -> ResultCode:
        """Send Slack message

        Args:
            text (_type_, optional): Simple text. Defaults to None.
            blocks (list, optional): Rich text. Defaults to [].

        Returns:
            ResultCode: Result code
        """
        if not self.channel_id:
            return ResultCode.FAILED

        logger.info(f"Targetted channel: #{self.channel}[{self.channel_id}]")
        sent_blocks = (
            blocks
            if len(blocks) > 0
            else [{"type": "section", "text": {"type": "mrkdwn", "text": text}}]
        )

        message_id = f"mid: #{str(uuid.uuid4()).lower()}"
        sent_blocks.extend(
            [
                {"type": "divider"},
                {
                    "type": "context",
                    "elements": [
                        {"type": "plain_text", "text": message_id, "emoji": True}
                    ],
                },
            ]
        )

        try:
            _ = self.client.chat_postMessage(
                channel=self.channel_id,
                blocks=sent_blocks,
                text=f"{sent_blocks}{message_id}",
                unfurl_links=False,
                unfurl_media=False,
            )
        except SlackApiError as e:
            logger.error(f"Got an error: {e.response['error']}")
            return ResultCode.FAILED

        return ResultCode.SUCCEEDED

    def find_channel_id(self, name: str) -> str:
        """Find Slack channel ID by name

        Args:
            name (str): Channel name

        Returns:
            str: Channel ID
        """
        try:
            for result in self.client.conversations_list():
                for channel in result["channels"]:
                    if channel["name"] == name:
                        return channel["id"]
        except SlackApiError as e:
            logger.error(str(e))
            return None
