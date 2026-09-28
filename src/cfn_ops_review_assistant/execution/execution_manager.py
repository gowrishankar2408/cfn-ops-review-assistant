
'''Manage execution of CFN operations reviews.'''
from cfn_ops_review_assistant.llm.prompts import COMPARISON_PROMPT_TEMPLATE
from cfn_ops_review_assistant.models.models import ReviewResult
from cfn_ops_review_assistant.processes.pps_custom_expiration_review import PPSCustomExpirationReview
import cfn_ops_review_assistant.processes.psr_review as psr_review

class ExecutionManager:

    def execute(
        self,
        review_type: str,
        case_number: str,
        token: str,
    ):

        if review_type == "psr-review":
            summary_result = psr_review.review(case_number, token)
            return ReviewResult(
                case_number=case_number,
                process_name = "psr-review",
                summary=summary_result["summary"],
                status=summary_result["comparison_result"]["match"],
            )
            

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
        return psr_review.PSRReview().close_case(case_number, token)