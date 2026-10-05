from pathlib import Path
import shutil
import json

class PublishService:
    def load_candidate(self, request_id: str, capability_name: str) -> None:

        project_root = (Path(__file__).resolve().parents[3])
        candidate_dir = (
                    project_root
                    / "src"
                    / "cfn_ops_review_assistant"
                    / "capabilities"
                    / capability_name
                    / "candidates"
                )
        candidate_file = candidate_dir / f"{request_id}.json"

        if not candidate_file.exists():
            raise FileNotFoundError(
                f"Candidate file for request ID {request_id} not found."
            )

        with open(candidate_file, "r") as f:
            candidate_data = json.load(f)

        return candidate_data
    
    def promote_candidate(self, request_id: str, candidate_data: dict) -> None:

        project_root = (Path(__file__).resolve().parents[3])
        published_dir = (
                    project_root
                    / "src"
                    / "cfn_ops_review_assistant"
                    / "capabilities"
                    / candidate_data["name"]
                )
        candidate_version = candidate_data["version"].split('.')
        published_file = published_dir / f"v{candidate_version[0]}.json"
        candidate_file = (
                    project_root
                    / "src"
                    / "cfn_ops_review_assistant"
                    / "capabilities"
                    / candidate_data["name"]
                    / "candidates"
                    / f"{request_id}.json"
                )
        with open(candidate_file, "r") as f:
            candidate = json.load(f)

        published_artifact = candidate.copy()

        published_artifact.pop(
            "status",
            None,
        )

        published_artifact.pop(
            "generated_from",
            None,
        )

        published_artifact.pop(
            "analysis",
            None,
        )
        # Write the published artifact to the published file
        with open(published_file,"w",encoding="utf-8") as f:
            json.dump(
                published_artifact,
                f,
                indent=4,
            )
        '''
        shutil.copy(
                    candidate_file,
                    published_file,
                    )
                    '''
        meta_data_file = published_dir / "metadata.json"

        with open(meta_data_file, "w") as f:
            json.dump({
                "name": candidate_data["name"],
                "latest_version": f"{candidate_version[0]}.{candidate_version[1]}",
                "status": "active"
            }, f)
        return published_file