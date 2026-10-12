import os

from cfn_ops_review_assistant.llm.ollama_provider import OllamaProvider
from cfn_ops_review_assistant.llm.copilot_provider import CopilotProvider


def get_provider():

    provider = os.getenv(
        "discovery_provider",
        "ollama",
    ).lower()

    if provider == "copilot":

        return CopilotProvider(
            os.getenv(
                "copilot_secret"
            )
        )

    return OllamaProvider()