from __future__ import annotations

import argparse
from collections.abc import Sequence
from cfn_ops_review_assistant.services.token_service import Commlinksession
from cfn_ops_review_assistant.execution.execution_manager import ExecutionManager


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cfn-ops-review-assistant",
        description="CFN Operations Review Assistant",
    )

    parser.add_argument(
        "--review-type",
        choices=[
            "psr-review",
            "pps-custom-expiration",
        ],
        required=True,
    )

    parser.add_argument(
        "--case-number",
        required=True,
    )

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    token = Commlinksession('prod').session_creator()

    print("\nCFN Ops Review Assistant")
    print("-" * 50)

    print(f"Review Type : {args.review_type}")
    print(f"Case Number : {args.case_number}")
    print(f"Token       : {token}")

    ExecutionManager().execute(
        review_type=args.review_type,
        case_number=args.case_number,
        token=token)

    return 0