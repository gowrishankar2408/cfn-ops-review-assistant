from __future__ import annotations

import argparse
from collections.abc import Sequence

from cfn_ops_review_assistant.execution.execution_manager import ExecutionManager
from cfn_ops_review_assistant.services.token_service import Commlinksession
from cfn_ops_review_assistant.services.crm_service import CRMService
from cfn_ops_review_assistant.services.setup_service import SetupService
from cfn_ops_review_assistant.discovery.discovery_engine import DiscoveryEngine
from cfn_ops_review_assistant.discovery.publish_manager import PublishManager

def build_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(
        prog="cfn-ops-review-assistant",
        description="CFN Operations Review Assistant",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=False,
    )

    setup_parser = subparsers.add_parser(
        "setup",
        help="Install and validate local dependencies.",
    )

    review_parser = subparsers.add_parser(
        "review",
        help="Run a review process.",
    )

    review_parser.add_argument(
        "--review-type",
        choices=[
            "psr-review",
            "pps-custom-expiration",
        ],
        required=True,
    )

    review_parser.add_argument(
        "--case-number",
        required=True,
    )

    discover_parser = subparsers.add_parser(
            "discover",
            help="Run discovery for a discovery request.",
        )
        
    discover_parser.add_argument(
            "--request-id",
            required=True,
        )

    publish_parser = subparsers.add_parser(
                "publish",
                help="Publish a candidate capability.",
            )
            
    publish_parser.add_argument(
                "--request-id",
                required=True,
            )
    
    publish_parser.add_argument(
                    "--capability-name",
                    required=True,
                )

    return parser


def show_menu() -> tuple[str, str] | None:

    print("\n")
    print("=" * 50)
    print("      CFN Ops Review Assistant")
    print("=" * 50)

    print("\nAvailable Reviews\n")

    print("1. PSR Review")
    print("2. PPS Custom Expiration Review")
    print("3. Exit")

    selection = input(
        "\nSelect Review: "
    ).strip()

    review_mapping = {
        "1": "psr-review",
        "2": "pps-custom-expiration",
    }

    if selection == "3":
        return None

    review_type = review_mapping.get(selection)

    if not review_type:
        raise ValueError(
            "Invalid review selection."
        )

    case_number = input(
        "\nEnter Case Number: "
    ).strip()

    return review_type, case_number


def _run_review(review_type: str, case_number: str) -> int:

    print("\nGenerating CFN Session...")

    token = (
        Commlinksession('prod')
        .session_creator()
    )

    print("CFN Session Generated")

    try:

        result = (
            ExecutionManager()
            .execute(
                review_type=review_type,
                case_number=case_number,
                token=token,
            )
        )
    except RuntimeError as ex:
        print("\n")
        print("=" * 50)
        print("Review Failed")
        print("=" * 50)

        print(str(ex))

        print(
            "\nA discovery request has been created "
            "and assigned to the support team."
        )
        return 1

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
        if status_code == 204:
            print("\nCase closed successfully.")
        else:
            print("\nFailed to close the case.")

    else:

        print(
            "\nCase remains open."
        )

    return 0


def main(
    argv: Sequence[str] | None = None,
) -> int:

    parser = build_parser()

    args = parser.parse_args(argv)
    if args.command == "setup": 
        SetupService().run()
        return 0

    if args.command == "discover":
        DiscoveryEngine().discover(args.request_id)
        return 0
    
    if args.command == "publish":
        PublishManager().publish(args.request_id, args.capability_name)
        return 0

    if args.command == "review":
        return _run_review(args.review_type, args.case_number)

    while True:
        selection = show_menu()
        if selection is None:
            return 0

        _run_review(*selection)


if __name__ == "__main__":
    raise SystemExit(main())