from pathlib import Path
import json

from cfn_ops_review_assistant.capabilities.registry import CapabilityRegistry

class CandidateGenerator:

    def generate(
        self,
        capability_name: str,
        current_version: str,
        artifact: dict,
        request_id: str,
        incident_id: str,
        analysis: str,
    ):

        # Load discovery analysis

        analysis = json.load(open(analysis))

        # Create candidate from current artifact
        candidate = artifact.copy()

        # Versioning
        candidate["version"] = (
                    CapabilityRegistry()
                    .get_next_version(
                    capability_name)
                    )
        candidate["status"] = "candidate"

        # Traceability
        candidate["generated_from"] = {
            "request_id": request_id,
            "incident_id": incident_id,
        }

        candidate["analysis"] = analysis

        # Apply capability changes proposed by discovery
        for change in analysis.get(
            "artifact_changes",
            []
        ):

            current = change.get(
                "current",
                {}
            )

            proposed = change.get(
                "proposed",
                {}
            )

            for step in candidate.get(
                "steps",
                []
            ):

                target = step.get(
                    "target",
                    {}
                )

                if (
                    target.get("role")
                    == current.get("role")
                    and
                    target.get("name")
                    == current.get("name")
                ):

                    print(
                        "Applying artifact change:"
                    )
                    print(
                        f"Current: {current}"
                    )
                    print(
                        f"Proposed: {proposed}"
                    )

                    step["target"] = proposed

        # Candidate location
        project_root = (
            Path(__file__)
            .resolve()
            .parents[3]
        )

        candidate_dir = (
            project_root
            / "src"
            / "cfn_ops_review_assistant"
            / "capabilities"
            / capability_name
            / "candidates"
        )

        candidate_dir.mkdir(
            parents=True,
            exist_ok=True,
        )
        # Get the major version of the candidate
        candidate_version = candidate["version"].split(".")
        candidate_version = candidate_version[0]
        candidate_file = (
            candidate_dir
            / f"{request_id}.json"
        )

        with open(
            candidate_file,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                candidate,
                f,
                indent=4,
            )

        return candidate_file