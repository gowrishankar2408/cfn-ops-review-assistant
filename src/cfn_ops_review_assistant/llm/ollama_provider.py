from .provider import LLMProvider
from cfn_ops_review_assistant.llm.ollama_client import OllamaClient


class OllamaProvider(
    LLMProvider
):

    def __init__(self):

        self.client = OllamaClient()

    def generate(
        self,
        prompt: str,
    ) -> str:

        return self.client.chat(
            prompt
        )