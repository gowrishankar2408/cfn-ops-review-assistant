from cfn_ops_review_assistant.utils.path_utils import get_project_root
from pathlib import Path
import json

class IncidentLoader:
    def load(
            self,
            incident_id: str,
        ):

            incident_dir = (
                get_project_root()
                / "logs"
                / "incidents"
                / "reports"
            )

            request_file = (
                incident_dir
                / f"{incident_id}.json"
            )

            if not request_file.exists():

                raise FileNotFoundError(
                    f"Incident not found: {incident_id}"
                )

            with open(
                request_file,
                encoding="utf-8",
            ) as f:

                return json.load(f)