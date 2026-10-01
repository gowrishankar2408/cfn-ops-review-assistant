from cfn_ops_review_assistant.discovery.discovery_manager import DiscoveryManager
from cfn_ops_review_assistant.incidents.incidents_loader import IncidentLoader
from pprint import pprint
import json
from cfn_ops_review_assistant.capabilities.registry import CapabilityRegistry
from cfn_ops_review_assistant.discovery.context_builder import DiscoveryContextBuilder
from cfn_ops_review_assistant.discovery.discovery_analyzer import DiscoveryAnalyzer
from cfn_ops_review_assistant.discovery.candidate_generator import CandidateGenerator

class DiscoveryEngine:

    def discover(
        self,
        request_id: str,
    ):
        print("=" * 50)
        print(
            f"Starting discovery for {request_id}"
        )
        print("=" * 50)

        #get particular request details
        request = (
            DiscoveryManager()
            .get_request(
                request_id
            )
        )
        print("=" * 50)
        print(f"Request details: {request}")
        print("=" * 50)

        #using the incident loader to get incident details
        incident = (
                    IncidentLoader()
                    .load(
                        request["incident_id"]
                    )
                )
        print("=" * 50)
        print(f"Incident details: {incident}")
        print("=" * 50)

        #extracting the screenshot path from the incident details
        screenshot_path = incident["screenshot"]
        print("=" * 50)
        print(f"Screenshot: {screenshot_path}")
        print("=" * 50)

        #resolving the capability from the registry
        registry = CapabilityRegistry()
        capability = registry.resolve(
            request["capability"]
        )
        print("=" * 50)
        print(f"Capability Name: {capability.name}")
        print(f"Capability Version: {capability.version}")
        print("=" * 50)

        #loading the artifact for the capability
        artifact = (
            CapabilityRegistry()
            .load_artifact(
                capability.name
            )
        )
        print("=" * 50)
        print(f"Artifact loaded: {artifact}")
        print("=" * 50)

        #building the discovery context and saving it to a file
        context_file = (
            DiscoveryContextBuilder()
            .build(
                request=request,
                incident=incident,
                capability_name=capability.name,
                version=capability.version,
                screenshot_path=screenshot_path,
                artifact=artifact,
            )
        )
        print("=" * 50)
        print(f"Context file created at: {context_file}")
        print("=" * 50)

        #analyzing the discovery context
        discovery_analysis = (
                    DiscoveryAnalyzer()
                    .analyze(
                        context=json.load(open(context_file))
                    )
                )
        print("=" * 50)
        print(
            f"Discovery analysis completed: {discovery_analysis}"
        )
        print("=" * 50)

        #generating the candidate capability based on the discovery analysis and the loaded artifact
        candidate_file = (
            CandidateGenerator()
            .generate(
                capability_name=capability.name,
                current_version=capability.version,
                artifact=artifact,
                analysis=discovery_analysis,
                request_id=request["request_id"],
                incident_id=incident["incident_id"],
            )
        )
        print("=" * 50)
        print(
                f"Candidate Capability Created: "
                f"{candidate_file}"
                )
        print("=" * 50)