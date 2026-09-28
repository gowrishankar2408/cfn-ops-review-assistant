from __future__ import annotations

import argparse
from collections.abc import Sequence

from cfn_ops_review_assistant.execution.execution_manager import (
    ExecutionManager,
)
from cfn_ops_review_assistant.services.token_service import (
    Commlinksession,
)
from cfn_ops_review_assistant.services.crm_service import (
    CRMService,
)


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
    )

    parser.add_argument(
        "--case-number",
    )

    return parser


def show_menu() -> tuple[str, str]:

    print("\n")
    print("=" * 50)
    print("      CFN Ops Review Assistant")
    print("=" * 50)

    print("\nAvailable Reviews\n")

    print("1. PSR Review")
    print("2. PPS Custom Expiration Review")

    selection = input(
        "\nSelect Review: "
    ).strip()

    review_mapping = {
        "1": "psr-review",
        "2": "pps-custom-expiration",
    }

    review_type = review_mapping.get(
        selection
    )

    if not review_type:
        raise ValueError(
            "Invalid review selection."
        )

    case_number = input(
        "\nEnter Case Number: "
    ).strip()

    return review_type, case_number


def main(
    argv: Sequence[str] | None = None,
) -> int:

    parser = build_parser()

    args = parser.parse_args(argv)

    if args.review_type and args.case_number:

        review_type = args.review_type
        case_number = args.case_number

    else:

        review_type, case_number = show_menu()

    print("\nGenerating CFN Session...")

    token = (
        Commlinksession('prod')
        .session_creator()
    )

    print("CFN Session GeneratedN")

    result = (
        ExecutionManager()
        .execute(
            review_type=review_type,
            case_number=case_number,
            token=token,
        )
    )

    print("\n")
    print(result.summary)
    print("\n")

    approval = input(
        "Do you want to close this case? (Y/N): "
    ).strip().upper()

    if approval == "Y":

        status_code = (
            ExecutionManager()
            .close_case(
                case_number=case_number,
                token=token,
            )
        )
        print(status_code)
        if status_code == 200:
            print("\nCase closed successfully.")
        else:
            print("\nFailed to close the case.")

    else:

        print(
            "\nCase remains open."
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())