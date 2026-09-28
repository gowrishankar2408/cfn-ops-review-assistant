"""Configuration helpers."""

import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv(Path(__file__).resolve().parents[3] / ".env")


def get_config(key: str, default: str | None = None) -> str | None:
    return os.getenv(key, default)
