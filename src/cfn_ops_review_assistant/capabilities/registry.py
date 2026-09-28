"""Capability registry definitions."""

CAPABILITIES = {
    "psr_review": "cfn_ops_review_assistant.processes.psr_review",
    "pps_custom_expiration_review": "cfn_ops_review_assistant.processes.pps_custom_expiration_review",
}


def list_capabilities() -> list[str]:
    return sorted(CAPABILITIES)
