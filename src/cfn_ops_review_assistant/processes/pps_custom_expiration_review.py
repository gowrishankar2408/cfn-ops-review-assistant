'''PPS Custom Expiration Review Process'''
import os
import requests

from cfn_ops_review_assistant.services.crm_service import CRMService
from cfn_ops_review_assistant.models.models import ReviewResult
from cfn_ops_review_assistant.services.surface_helper import SurfaceAdapter



def review(case_number: str, token: str) -> ReviewResult:
    process = CRMService()
    adaptor = SurfaceAdapter()
    try:
        current_step = "launch_case"
        adaptor.launch_case(
            case_number,
            token,
            )
        current_step = {
                    "action": "click",
                    "target": {
                        "role": "link",
                        "name": "Validate"
                    }
                }

        adaptor.click_edit()
        current_step = {
                    "action": "check",
                    "target": {
                        "role": "checkbox",
                        "name": "Exception Granted"
                    }
                }
        adaptor.select_exception_granted()
        current_step = {
                    "action": "click",
                    "target": {
                        "role": "button",
                        "name": "Update Case"
                    }
                }
        adaptor.click_update_case()
        current_step = "validate_exception_granted"
        success = adaptor.validate_exception_granted()
        return ReviewResult(
            case_number=case_number,
            process_name="pps-custom-expiration",
            status='Pass' if success else 'Fail',
            summary="PPS Custom Expiration Review completed." if success else "PPS Custom Expiration Review failed.",
            comparison_result={},
        )
    except Exception as ex:
        print("Exception occurred.")
        ex.failed_step = current_step
        ex.capture_url = adaptor.capture_url(case_number)
        ex.visible_controls = adaptor.get_visible_controls(case_number)
        #ex.page_text = adaptor.capture_page_text(case_number)
        ex.screenshot_path = (adaptor.capture_screenshot(case_number))

        raise
    finally:
        adaptor.close()