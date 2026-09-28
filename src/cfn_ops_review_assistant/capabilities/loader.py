"""Utility for loading capability implementations."""

from importlib import import_module


def load_capability(module_path: str):
    module = import_module(module_path)
    return getattr(module, "run_review")
