"""Structured result model for review workflows."""

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class ReviewResult:
    """Represents a review outcome."""

    capability: str
    status: str
    summary: str
    recommendations: List[str] = field(default_factory=list)
    evidence: Dict[str, Any] = field(default_factory=dict)
