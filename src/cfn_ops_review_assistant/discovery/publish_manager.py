from cfn_ops_review_assistant.discovery.discovery_manager import DiscoveryManager

from cfn_ops_review_assistant.services.publish_service import PublishService


class PublishManager:

    def publish(
        self,
        request_id: str,
        capability_name: str,
    ):

        print("=" * 50)
        print(
            f"Publishing candidate for request: "
            f"{request_id}"
        )
        print("=" * 50)

        service = PublishService()

        candidate = (
            service.load_candidate(
                request_id=request_id,
                capability_name=capability_name,
            )
        )

        published_file = (
            service.promote_candidate(
                request_id=request_id,
                candidate_data=candidate,
            )
        )

        print()
        print(
            f"Published: {published_file}"
        )

        print(
            f"Capability: {capability_name}"
        )

        print(
            f"Active Version: {candidate['version']}"
        )

        print(
            f"Discovery Request "
            f"{request_id} completed."
        )