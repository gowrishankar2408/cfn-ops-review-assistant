from cfn_ops_review_assistant.discovery.discovery_manager import DiscoveryManager
from cfn_ops_review_assistant.incidents.incidents_loader import IncidentLoader
from pprint import pprint
from cfn_ops_review_assistant.capabilities.registry import CapabilityRegistry
from cfn_ops_review_assistant.discovery.context_builder import DiscoveryContextBuilder

class DiscoveryEngine:

    def discover(
        self,
        request_id: str,
    ):

        print(
            f"Starting discovery for {request_id}"
        )

        #get particular request details
        request = (
            DiscoveryManager()
            .get_request(
                request_id
            )
        )
        print(request)

        #using the incident loader to get incident details
        incident = (
                    IncidentLoader()
                    .load(
                        request["incident_id"]
                    )
                )
        print(incident)

        #extracting the screenshot path from the incident details
        screenshot_path = incident["screenshot"]
        print(f"Screenshot: {screenshot_path}")

        #resolving the capability from the registry
        registry = CapabilityRegistry()
        capability = registry.resolve(
            request["capability"]
        )
        print(capability.name)
        print(capability.version)

        #building the discovery context and saving it to a file
        context_file = (
            DiscoveryContextBuilder()
            .build(
                request=request,
                incident=incident,
                capability_name=capability.name,
                version=capability.version,
                screenshot_path=screenshot_path,
            )
        )
        print(f"Context file created at: {context_file}")