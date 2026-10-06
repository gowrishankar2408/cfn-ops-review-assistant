from pathlib import Path
from cfn_ops_review_assistant.utils.path_utils import get_project_root
import sys

def get_capabilities_root() -> Path:

    # Running as EXE
    if getattr(sys, "frozen", False):
        return (
            get_project_root()
            / "capabilities"
        )

    # Running from source
    return (
        get_project_root()
        / "src"
        / "cfn_ops_review_assistant"
        / "capabilities"
    )