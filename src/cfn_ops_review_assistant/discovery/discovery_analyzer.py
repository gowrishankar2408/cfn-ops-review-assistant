from cfn_ops_review_assistant.llm.discovery_prompts import DISCOVERY_PROMPT
from cfn_ops_review_assistant.llm.ollama_client import OllamaClient
from pathlib import Path
import json
class DiscoveryAnalyzer:

    def analyze(
        self,
        context: dict,
    ):
        print("=" * 50)
        print(context["failed_step"])
        print("=" * 50)

        print(context["artifact"])
        prompt = DISCOVERY_PROMPT.format(
            capability=context["capability"],
            version=context["version"],
            incident_id=context["incident_id"],
            error=context["error"],
            artifact=context["artifact"],
            failed_step=context["failed_step"],
            visible_controls=context["visible_controls"]
            
        )
        print("=" * 50)
        print(prompt)
        print("=" * 50)
        response = (
            OllamaClient()
            .chat(prompt)
            )
        print(response)
        analysis = json.loads(response)
        print(analysis)
        project_root = (Path(__file__).resolve().parents[3])
        analysis_dir = (
            project_root
            / "logs"
            / "discovery"
            / "analysis"
        )
        analysis_file = (
                analysis_dir
                / f"{context['request_id']}.json"
                )
        analysis_dir.mkdir(parents=True, exist_ok=True)
        with open(analysis_file, "w") as f:
            json.dump(analysis, f)
        return analysis_file