import sys
from pathlib import Path


def get_project_root() -> Path:

    # Running from EXE
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent

    # Running from source
    return Path(__file__).resolve().parents[3]