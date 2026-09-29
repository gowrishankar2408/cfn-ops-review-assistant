from cfn_ops_review_assistant.capabilities.capability_health import CapabilityHealth

health = CapabilityHealth()

stats = health.get_stats(
    "pps-custom-expiration"
)

print(stats)