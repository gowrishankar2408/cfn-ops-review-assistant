from cfn_ops_review_assistant.capabilities.capability import Capability

import cfn_ops_review_assistant.processes.pps_custom_expiration_review as pps_review


class PPSCustomExpirationCapability(
    Capability
):

    @property
    def name(self):
        return "pps-custom-expiration"

    @property
    def version(self):
        return "1.0"

    def execute(
        self,
        case_number,
        token,
    ):
        return pps_review.review(
            case_number,
            token,
        )