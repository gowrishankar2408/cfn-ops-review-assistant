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
        screenshot: str | None = None,
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

            "screenshot":
                screenshot,
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