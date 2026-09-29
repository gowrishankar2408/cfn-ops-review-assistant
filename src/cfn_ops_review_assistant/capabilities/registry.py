from cfn_ops_review_assistant.capabilities.psr_review_capability import PSRReviewCapability
from cfn_ops_review_assistant.capabilities.pps_custom_expiration_capability import PPSCustomExpirationCapability


class CapabilityRegistry:

    def resolve(
        self,
        capability_name: str,
    ):

        capability_map = {
            "psr-review":
                PSRReviewCapability(),

            "pps-custom-expiration":
                PPSCustomExpirationCapability(),
        }

        return capability_map[
            capability_name
        ]