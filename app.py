from __future__ import annotations

import argparse
import json

from src.workflows import run_workflow


def main() -> None:
    parser = argparse.ArgumentParser(description="AI CRM automation workflow demo")
    parser.add_argument(
        "--workflow",
        choices=[
            "proposal_qa",
            "site_summary",
            "bill_extract",
            "ghl_onboarding",
            "zapier_repair",
            "email_funnel",
            "dashboard_snapshot",
        ],
        default="ghl_onboarding",
    )
    args = parser.parse_args()
    result = run_workflow(args.workflow)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
