from pathlib import Path
from datetime import datetime
from cfn_ops_review_assistant.utils.path_utils import get_project_root
import json


class ExecutionLogger:

    def log(
        self,
        log_record: dict,
    ):
        project_root = get_project_root()
        log_dir = project_root / "logs/executions"

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