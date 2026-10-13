import os
from dotenv import load_dotenv
import urllib3
from .provider import LLMProvider
import requests
import time
from cfn_ops_review_assistant.utils.path_utils import get_project_root
load_dotenv(get_project_root() / ".env")
urllib3.disable_warnings()

class CopilotProvider(
    LLMProvider
):

    def __init__(
        self,
        secret: str,
    ):
        self.secret = os.getenv("pps_copilot_secret")

    def generate(
        self,
        prompt: str,
    ) -> str:

        headers = {
            "Authorization":
                f"Bearer {self.secret}"
        }
        conversation = requests.post(os.getenv("copilot_url"),
            headers=headers,
            verify=False
        ).json()

        conversation_id = (
            conversation["conversationId"]
            if "conversationId" in conversation
            else conversation["conversation"]["id"]
        )
        #print(f"Id {conversation_id}")

        payload = {
            "type": "message",
            "from": {
                "id": "discovery-agent"
            },
            "text": prompt,
        }

        requests.post(os.getenv("copilot_url") + f"/{conversation_id}/activities",
            headers=headers,
            json=payload,
            verify=False
        )

        time.sleep(5)

        activities = requests.get(
            os.getenv("copilot_url") + f"/{conversation_id}/activities",
            headers=headers,
            verify=False
        ).json()
        #print(f"Activities: {activities}")

        messages = [
                activity.get("text")
                for activity in activities["activities"]
                if (
                    activity.get("type") == "message"
                    and activity.get("text")
                    and activity.get("from", {}).get("id")
                    != "discovery-agent"
                )
            ]

        return messages[-1]