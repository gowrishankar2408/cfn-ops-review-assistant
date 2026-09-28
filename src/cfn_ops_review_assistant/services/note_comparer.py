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
        """
        print("\nPrompt Sent:")
        print(prompt)
        
        print("\nRaw Model Response:")
        print(repr(response))
        """
        print(repr(response))
        return json.loads(response)