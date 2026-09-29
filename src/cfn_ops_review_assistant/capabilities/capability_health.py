import json

from pathlib import Path

from cfn_ops_review_assistant.models.capability_healthcheck_model import CapabilityHealthResult

class CapabilityHealth:

    def get_stats(
        self,
        capability_name: str,
    ) -> CapabilityHealthResult:
        log_file = (
            Path(__file__)
            .resolve()
            .parents[3]
            / "logs"
            / "executions"
        )
        log_files = log_file.glob("*.jsonl")
        total = 0
        success = 0
        fail = 0

        if not log_file.exists():
            
            return CapabilityHealthResult(
                capability=capability_name,
                total_executions=0,
                success_count=0,
                failure_count=0,
                log_file=str(log_file),
                success_rate=0,
            )
        
        for log_file in log_files:
            with open(
                log_file,
                encoding="utf-8",
            ) as f:

                for line in f:

                    record = json.loads(line)

                    if (
                        record["capability"]
                        != capability_name
                    ):
                        continue

                    total += 1

                    if (
                        record["status"]
                        in (
                            "Pass",
                            "Matching",
                            "SUCCESS",
                        )
                    ):
                        success += 1

                    else:
                        fail += 1

            rate = (
                (success / total) * 100
                if total
                else 0
            )
            return CapabilityHealthResult(
                capability=capability_name,
                total_executions=total,
                success_count=success,
                failure_count=fail,
                log_file=str(log_file),
                success_rate=round(
                    rate,
                    2,
                ),
            )