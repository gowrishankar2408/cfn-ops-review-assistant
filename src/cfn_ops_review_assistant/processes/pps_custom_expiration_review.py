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
        adaptor.launch_case(
            case_number,
            token,
            )
        adaptor.click_edit()
        adaptor.select_exception_granted()
        adaptor.click_update_case()
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
        screenshot_path = (
            adaptor.capture_screenshot(
                case_number
            )
        )
        print(
                f"Screenshot Path: {screenshot_path}"
                )
        ex.screenshot_path = screenshot_path
        raise
    finally:
        adaptor.close()