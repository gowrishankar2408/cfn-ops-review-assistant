
'''Manage execution of CFN operations reviews.'''
from cfn_ops_review_assistant.llm.prompts import COMPARISON_PROMPT_TEMPLATE
from cfn_ops_review_assistant.models.models import ReviewResult
import cfn_ops_review_assistant.processes.psr_review as psr_review
import cfn_ops_review_assistant.processes.pps_custom_expiration_review as pps_custom_review
from cfn_ops_review_assistant.services.crm_service import CRMService
from cfn_ops_review_assistant.capabilities.registry import CapabilityRegistry
from cfn_ops_review_assistant.replay.replay_engine import ReplayEngine

class ExecutionManager:

    def execute(
        self,
        review_type: str,
        case_number: str,
        token: str,
    ):
        capability = (CapabilityRegistry().resolve(review_type)) 
        return ReplayEngine().execute(capability, case_number,token, )
        '''
        if review_type == "psr-review":
            summary_result = psr_review.review(case_number, token)
            return summary_result
            

        elif review_type == "pps-custom-expiration":
            summary_result = pps_custom_review.review(case_number, token)
            return summary_result
        '''
        
    def close_case(
    self,
    case_number: str,
    token: str,
):
        return CRMService().close_case(case_number, token)