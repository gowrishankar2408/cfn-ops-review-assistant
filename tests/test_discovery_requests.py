from cfn_ops_review_assistant.discovery.discovery_manager import DiscoveryManager

manager = DiscoveryManager()

requests = (
    manager.get_pending_requests()
)

print(requests)