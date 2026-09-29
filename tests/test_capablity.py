from cfn_ops_review_assistant.capabilities.registry import CapabilityRegistry

registry = CapabilityRegistry()

capability = registry.load(
    "psr-review"
)

print(capability)