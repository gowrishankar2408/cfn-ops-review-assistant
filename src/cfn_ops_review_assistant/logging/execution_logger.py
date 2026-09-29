from pathlib import Path
from datetime import datetime
import json


class ExecutionLogger:

    def log(
        self,
        log_record: dict,
    ):

        log_dir = Path("logs/executions")

        log_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_name = (
            datetime.now()
            .strftime("%Y-%m-%d")
            + ".jsonl"
        )

        log_file = log_dir / file_name

        with open(
            log_file,
            "a",
            encoding="utf-8",
        ) as f:

            f.write(
                json.dumps(log_record)
                + "\n"
            )