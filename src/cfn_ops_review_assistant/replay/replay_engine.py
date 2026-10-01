from cfn_ops_review_assistant.logging.execution_logger import ExecutionLogger
from cfn_ops_review_assistant.incidents.incidents import IncidentManager
from cfn_ops_review_assistant.discovery.discovery_manager import DiscoveryManager
from datetime import datetime
from pathlib import Path
import json

class ReplayEngine:

    def execute(
        self,
        capability,
        case_number,
        token,
    ):

        print(
            f"Executing capability "
            f"{capability.name} "
            f"v{capability.version}"
        )
        try:

            result = capability.execute(
                case_number,
                token,
            )
            ExecutionLogger().log(
                {
                "case_number": case_number,
                "capability": capability.name,
                "version": capability.version,
                "status": result.status,
                "result": result.summary,
                "timestamp": datetime.now().isoformat(),
                }
                )
            return result
        except Exception as e:
            print("Creating incident...")
            screenshot = getattr(e,"screenshot_path",None,)
            failed_step = getattr(e,"failed_step",None)
            capture_url = getattr(e,"capture_url",None)
            page_text = getattr(e,"page_text",None)
            visible_controls = getattr(e,"visible_controls",None)
            incident_id = IncidentManager().create(
            capability=capability.name,
            version=capability.version,
            case_number=case_number,
            error=str(e),
            failed_step=failed_step,
            screenshot=screenshot,
            capture_url=capture_url,
            #page_text=page_text,
            visible_controls=visible_controls,
            )
            discovery_request_id = (DiscoveryManager().create_request(
                        capability=capability.name,
                        version=capability.version,
                        incident_id=incident_id,
                        case_number=case_number,
                    )
                )
            print("Writing failure log...")
            ExecutionLogger().log(
                {
                "case_number": case_number,
                "capability": capability.name,
                "version": capability.version,
                "status": "Fail",
                "result": str(e),
                "timestamp": datetime.now().isoformat(),
                "incident_id": incident_id,
                "discovery_request_id": discovery_request_id,
                }
                )
            print("Failure log written.")
            raise RuntimeError(
            f"Execution failed. "
            f"Incident: {incident_id}"
            f" Discovery Request: {discovery_request_id}"
            ) from e