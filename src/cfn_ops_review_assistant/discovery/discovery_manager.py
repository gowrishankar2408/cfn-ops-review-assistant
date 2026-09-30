import json
import uuid

from pathlib import Path
from datetime import datetime


class DiscoveryManager:

    def create_request(
        self,
        capability: str,
        version: str,
        incident_id: str,
        case_number: str,
    ) -> str:

        request_id = (
            f"DISC-{uuid.uuid4()}"
        )

        payload = {
            "request_id": request_id,
            "capability": capability,
            "version": version,
            "incident_id": incident_id,
            "case_number": case_number,
            "status": "pending",
            "created_at": (
                datetime.now()
                .isoformat()
            ),
        }

        project_root = (
            Path(__file__)
            .resolve()
            .parents[3]
        )

        request_dir = (
            project_root
            / "logs"
            / "discovery"
            / "requests"
        )

        request_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(
            request_dir / f"{request_id}.json",
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                payload,
                f,
                indent=2,
            )

        return request_id

    def get_pending_requests(
            self,
        ):
            requests = []
            request_dir = (
                        Path(__file__).resolve().parents[3]
                        / "logs"
                        / "discovery"
                        / "requests"
                    )
            if not request_dir.exists():
                return []
    
            for request_file in request_dir.glob("*.json"):
                with open(request_file,encoding="utf-8",) as f:
                    request = json.load(f)
                if request["status"] == "pending":
                    requests.append(request)
            return requests