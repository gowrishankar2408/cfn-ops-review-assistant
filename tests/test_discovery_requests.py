from cfn_ops_review_assistant.discovery.discovery_manager import DiscoveryManager

manager = DiscoveryManager()

requests = (
    manager.mark_completed("DISC-06239b2a-5550-437f-a8a7-3b1a4338bf05")
)

print(requests)