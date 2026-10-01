from datetime import datetime
import json
from pathlib import Path

class DiscoveryContextBuilder:

    def build(
        self,
        request: dict,
        incident: dict,
        capability_name: str,
        version: str,
        screenshot_path: str,
        artifact: str,
    ):
        context = {

            "request_id":
                request["request_id"],

            "capability":
                capability_name,

            "version":
                version,

            "incident_id":
                incident["incident_id"],

            "case_number":
                incident["case_number"],

            "error":
                incident["error"],

            "screenshot":
                screenshot_path,

            "failed_step":
                incident["failed_step"],

            "capture_url":
                incident["capture_url"],

            "generated_at":
                datetime.now().isoformat(),

            "artifact":
                artifact,

            "visible_controls":
                incident["visible_controls"],
        }
        project_root = (Path(__file__).resolve().parents[3])
        context_dir = (
            project_root
            / "logs"
            / "discovery"
            / "contexts"
        )
        context_dir.mkdir(
            parents=True,
            exist_ok=True,
        )
        context_file = (
            context_dir
            / f"{request['request_id']}.json"
        )
        with open(context_file, "w") as f:
            json.dump(context, f, indent=2)
        return context_file