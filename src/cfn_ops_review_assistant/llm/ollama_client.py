"""Ollama client placeholder."""


class OllamaClient:
    """Simple wrapper to an Ollama endpoint."""

    def __init__(self, endpoint: str = "http://localhost:11434"):
        self.endpoint = endpoint

    def ping(self) -> bool:
        return bool(self.endpoint)
