from cfn_ops_review_assistant.capabilities.capability import Capability

import cfn_ops_review_assistant.processes.psr_review as psr_review


class PSRReviewCapability(
    Capability
):

    @property
    def name(self):
        return "psr-review"

    @property
    def version(self):
        return "1.0"

    def execute(
        self,
        case_number,
        token,
    ):

        return psr_review.review(
            case_number,
            token,
        )