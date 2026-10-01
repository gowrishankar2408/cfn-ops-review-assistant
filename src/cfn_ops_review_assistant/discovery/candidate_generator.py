from pathlib import Path
import json

class CandidateGenerator:

    def generate(
        self,
        capability_name: str,
        current_version: str,
        artifact: dict,
        request_id: str,
        incident_id: str,
        analysis: dict,
    ):
        project_root = (Path(__file__).resolve().parents[3])
        candidate_dir = (
            project_root
            / "logs"
            / "discovery"
            / "candidates"
        )
        candidate_file = (
                candidate_dir
                / f"{request_id}.json"
                )
        print(candidate_file)
        candidate_dir.mkdir(parents=True, exist_ok=True)
        artifacts_content = {
                                "capability": capability_name,
                                "current_version": current_version,
                                "candidate_version": "2.0",
                                "status": "candidate",
                                "generated_from": {"request_id": request_id,
                                                    "incident_id": incident_id
                                                },
                                "analysis": json.load(open(analysis)),
                                "current_artifact": artifact
                            }
        with open(candidate_file, "w") as f:
            json.dump(artifacts_content, f)

        return candidate_file