
'''Manage execution of CFN operations reviews.'''
from cfn_ops_review_assistant.llm.prompts import COMPARISON_PROMPT_TEMPLATE
from cfn_ops_review_assistant.models.models import ReviewResult
from cfn_ops_review_assistant.processes.pps_custom_expiration_review import PPSCustomExpirationReview
import cfn_ops_review_assistant.processes.psr_review as psr_review
from cfn_ops_review_assistant.services.crm_service import CRMService

class ExecutionManager:

    def execute(
        self,
        review_type: str,
        case_number: str,
        token: str,
    ):

        if review_type == "psr-review":
            summary_result = psr_review.review(case_number, token)
            return summary_result
            

        elif review_type == "pps-custom-expiration":
            PPSCustomExpirationReview().execute(
                case_number,
                token,
            )

    def close_case(
        self,
        case_number: str,
        token: str,
    ):
        return CRMService().close_case(case_number, token)