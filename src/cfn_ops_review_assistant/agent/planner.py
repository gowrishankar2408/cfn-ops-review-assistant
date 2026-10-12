import requests
from cfn_ops_review_assistant.llm.ollama_client import OllamaClient


class Planner:

    def __init__(self):

        self.llm = OllamaClient()

    def decide(
        self,
        goal: str,
        state: dict,
    ) -> dict:

        prompt = f"""
You are a UI automation agent.

Goal:
{goal}

Current URL:
{state["url"]}

Visible Controls:

{state["controls"]}

Choose the single best next action.

Return ONLY JSON.

Example:

{{
    "action": "click",
    "target": {{
        "role": "link",
        "name": "Edit",
        "description": "Open case in edit mode to modify values",
        "children": ["Edit", "Actions"]
    }}
}}
"""
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.1-local",
                "prompt": prompt,
                "stream": False,
            },
            timeout=120,
        )
        response.raise_for_status()

        return response.json()["response"]