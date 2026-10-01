import json
import uuid

from pathlib import Path
from datetime import datetime


class IncidentManager:

    def create(
        self,
        capability: str,
        version: str,
        case_number: str,
        error: str,
        failed_step: str,
        capture_url: str | None = None,
        screenshot: str | None = None,
        visible_controls: str | None = None,
    ) -> str:

        incident_id = (
            f"INC-{uuid.uuid4()}"
        )

        report = {

            "incident_id":
                incident_id,

            "capability":
                capability,

            "version":
                version,

            "case_number":
                case_number,

            "error":
                error,

            "timestamp":
                datetime.now().isoformat(),

            "failed_step":
                failed_step,

            "screenshot":
                screenshot,
                
            "visible_controls":
                visible_controls,

            "capture_url":
                capture_url,
        }
        base_dir = Path(__file__).resolve().parents[3]
        reports_dir = (base_dir /"logs" /"incidents" /"reports"
        )
        print(f"Writing to: {reports_dir}")

        reports_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        report_file = (
            reports_dir
            / f"{incident_id}.json"
        )

        with open(
            report_file,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                report,
                f,
                indent=2,
            )

        return incident_id