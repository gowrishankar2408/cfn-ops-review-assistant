import requests


class OllamaClient:

    def chat(
        self,
        prompt: str,
    ) -> str:

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