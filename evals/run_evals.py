from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.benchmark import score_model
from src.workflows import run_workflow


def main() -> None:
    workflows = [
        "proposal_qa",
        "site_summary",
        "bill_extract",
        "ghl_onboarding",
        "zapier_repair",
        "email_funnel",
        "dashboard_snapshot",
    ]
    results = [run_workflow(name) for name in workflows]
    assert all(row["audit"]["source_grounded"] for row in results)
    assert all(row["audit"]["raw_customer_data_sent"] is False for row in results)
    benchmark = [
        score_model("claude-sonnet-task-class", 0.91, 2200, 0.034),
        score_model("openai-gpt-task-class", 0.89, 1600, 0.026),
    ]
    print(json.dumps({"workflow_results": results, "benchmark": benchmark}, indent=2))


if __name__ == "__main__":
    main()
