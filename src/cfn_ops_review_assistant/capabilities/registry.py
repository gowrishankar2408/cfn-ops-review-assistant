from pathlib import Path
import json


class CapabilityRegistry:

    def load(
        self,
        capability_name: str,
    ):

        capability_path = (
                            Path(__file__).parent
                            / capability_name
                            / "metadata.json"
                        )
        
        print(capability_path)

        return json.loads(
            capability_path.read_text()
        )