from cfn_ops_review_assistant.capabilities.registry import CapabilityRegistry
registry = CapabilityRegistry()

metadata = registry.load_metadata(
    "pps-custom-expiration"
)

print(metadata)

artifact = registry.load_artifact(
    "pps-custom-expiration"
)

print(artifact)