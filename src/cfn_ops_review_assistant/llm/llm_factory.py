import os

from cfn_ops_review_assistant.llm.ollama_provider import OllamaProvider
from cfn_ops_review_assistant.llm.copilot_provider import CopilotProvider


def get_provider(agent_name: str):

    provider = os.getenv(
        "discovery_provider",
        "ollama",
    ).lower()

    if provider == "copilot":
        if agent_name.lower() == "pps":
            return CopilotProvider(
                os.getenv(
                    "pps_copilot_secret"
                )
            )
        if agent_name.lower() == "psr":
            print("Using PSR Copilot Provider")
            return CopilotProvider(
                os.getenv(
                    "psr_copilot_secret"
                )
            )

    return OllamaProvider()