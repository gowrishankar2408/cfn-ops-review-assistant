
'''Manage execution of CFN operations reviews.'''
from cfn_ops_review_assistant.processes.psr_review import PSRReview
from cfn_ops_review_assistant.processes.pps_custom_expiration_review import PPSCustomExpirationReview

class ExecutionManager:

    def execute(
        self,
        review_type: str,
        case_number: str,
        token: str,
    ):

        if review_type == "psr-review":
            PSRReview().execute(
                case_number,
                token,
            )

        elif review_type == "pps-custom-expiration":
            PPSCustomExpirationReview().execute(
                case_number,
                token,
            )