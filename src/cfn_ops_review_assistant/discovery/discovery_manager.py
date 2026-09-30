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


    def get_request(
        self,
        request_id: str,
    ):

        request_dir = (
            Path(__file__).resolve().parents[3]
            / "logs"
            / "discovery"
            / "requests"
        )

        request_file = (
            request_dir
            / f"{request_id}.json"
        )

        if not request_file.exists():

            raise FileNotFoundError(
                f"Discovery request not found: {request_id}"
            )

        with open(
            request_file,
            encoding="utf-8",
        ) as f:

            return json.load(f)

    def mark_in_progress(
    self,
    request_id: str,
):
        request = self.get_request(
            request_id
        )

        request["status"] = (
            "in-progress"
        )

        request_file = (
            Path(__file__).resolve().parents[3]
            / "logs"
            / "discovery"
            / "requests"
            / f"{request_id}.json"
        )

        with open(
            request_file,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                request,
                f,
                indent=2,
            )

    def mark_completed(
    self,
    request_id: str,
):

        request = self.get_request(
            request_id
        )

        request["status"] = (
            "completed"
        )

        request_file = (
            Path(__file__).resolve().parents[3]
            / "logs"
            / "discovery"
            / "requests"
            / f"{request_id}.json"
        )

        with open(
            request_file,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                request,
                f,
                indent=2,
            )

    def mark_rejected(
    self,
    request_id: str,
):
        request = self.get_request(
            request_id
        )

        request["status"] = (
            "rejected"
        )

        request_file = (
            Path(__file__).resolve().parents[3]
            / "logs"
            / "discovery"
            / "requests"
            / f"{request_id}.json"
        )

        with open(
            request_file,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                request,
                f,
                indent=2,
            )