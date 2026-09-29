import os
import subprocess
from pathlib import Path
import requests


class SetupService:

    def run(self):

        self.validate_browser()

        self.check_ollama()

        self.check_model()


    def validate_browser(self):

        browser_path = os.getenv(
            "PLAYWRIGHT_BROWSER_PATH"
        )

        if not browser_path:
            raise RuntimeError(
                "PLAYWRIGHT_BROWSER_PATH is not configured."
            )

        if not Path(browser_path).exists():
            raise RuntimeError(
                f"Browser not found: {browser_path}"
            )

        print("Chromium Found")

    def install_playwright(self):

        print(
            "\nInstalling Playwright Chromium..."
        )

        subprocess.run(
            [
                "playwright",
                "install",
                "chromium",
            ],
            check=True,
        )

        print(
            "Chromium Installed"
        )

    def check_ollama(self):

        print(
            "\nChecking Ollama..."
        )

        response = requests.get(
            "http://localhost:11434/api/tags",
            timeout=10,
        )

        response.raise_for_status()

        print(
            "Ollama Reachable"
        )

    def check_model(self):

        response = requests.get(
            "http://localhost:11434/api/tags",
            timeout=10,
        )

        models = response.json()

        found = any(
            model["name"].startswith(
                "llama3.1-local"
            )
            for model in models["models"]
        )

        if not found:
            raise RuntimeError(
                "llama3.1-local model not installed."
            )

        print(
            "llama3.1-local Found"
        )