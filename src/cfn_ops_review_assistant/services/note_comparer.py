import json
from urllib import response

from cfn_ops_review_assistant.llm.ollama_client import OllamaClient
from cfn_ops_review_assistant.llm.prompts import (
    COMPARISON_PROMPT_TEMPLATE,
)
class NoteComparer:

    def compare(
        self,
        original_note: str,
        edited_note: str,
    ) -> dict:

        prompt = COMPARISON_PROMPT_TEMPLATE.format(
            left_clean=original_note,
            right_clean=edited_note,
        )

        response = OllamaClient().chat(
            prompt=prompt
        )
        response = response.strip()
        if not response:
            raise RuntimeError(
            "LLM returned an empty response."
            )
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            print("\nFAILED TO PARSE JSON")
            print("RESPONSE:")
            print(repr(response))
            raise