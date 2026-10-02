import json
from pathlib import Path
from cfn_ops_review_assistant.capabilities.psr_review_capability import PSRReviewCapability
from cfn_ops_review_assistant.capabilities.pps_custom_expiration_capability import PPSCustomExpirationCapability


class CapabilityRegistry:

    def resolve(
        self,
        capability_name: str,
    ):

        capability_map = {
            "psr-review":
                PSRReviewCapability(),

            "pps-custom-expiration":
                PPSCustomExpirationCapability(),
        }

        return capability_map[
            capability_name
        ]

    def load_metadata(
        self,
        capability_name: str,
    ):
        project_root = (Path(__file__).resolve().parents[3])
        metadata_file = (
            project_root
            / "src"
            / "cfn_ops_review_assistant"
            / "capabilities"
            / capability_name
            / "metadata.json"
        )

        with open(metadata_file,encoding="utf-8",) as f:
            return json.load(f)
            

    def load_artifact(
    self,
    capability_name: str,
    ):
        metadata = self.load_metadata(
            capability_name
        )

        version = metadata[
            "latest_version"
        ]
        project_root = (Path(__file__).resolve().parents[3])
        artifact_file = (
            project_root
            / "src"
            / "cfn_ops_review_assistant"
            / "capabilities"
            / capability_name
            / f"v{version.split('.')[0]}.json"
        )

        with open(
            artifact_file,
            encoding="utf-8",
        ) as f:
            return json.load(f)

    def get_next_version(self,capability_name: str,) -> str:
        artifact = self.load_artifact(
            capability_name
        )

        current = artifact["version"]

        major, minor = current.split(".")

        return f"{int(major)+1}.0"