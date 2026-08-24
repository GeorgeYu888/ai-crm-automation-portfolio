from __future__ import annotations

import json
from pathlib import Path

from src.llm_clients import LocalDeterministicLLM
from src.privacy import redact_sensitive_text
from src.retrieval import retrieve
from src.schemas import (
    BILL_EXTRACT_SCHEMA,
    DASHBOARD_SNAPSHOT_SCHEMA,
    EMAIL_FUNNEL_SCHEMA,
    GHL_ONBOARDING_SCHEMA,
    PROPOSAL_QA_SCHEMA,
    SITE_SUMMARY_SCHEMA,
    ZAPIER_REPAIR_SCHEMA,
)


ROOT = Path(__file__).resolve().parents[1]
CRM_DIR = ROOT / "data" / "crm_records"

SCHEMAS = {
    "proposal_qa": PROPOSAL_QA_SCHEMA,
    "site_summary": SITE_SUMMARY_SCHEMA,
    "bill_extract": BILL_EXTRACT_SCHEMA,
    "ghl_onboarding": GHL_ONBOARDING_SCHEMA,
    "zapier_repair": ZAPIER_REPAIR_SCHEMA,
    "email_funnel": EMAIL_FUNNEL_SCHEMA,
    "dashboard_snapshot": DASHBOARD_SNAPSHOT_SCHEMA,
}


def load_record(workflow: str) -> dict:
    return json.loads((CRM_DIR / f"{workflow}.json").read_text(encoding="utf-8"))


def run_workflow(workflow: str) -> dict:
    record = load_record(workflow)
    raw_text = json.dumps(record, indent=2)
    safe_text, redactions = redact_sensitive_text(raw_text)
    sources = retrieve(safe_text)
    prompt = f"CRM input:\n{safe_text}\n\nApproved knowledge:\n{json.dumps(sources, indent=2)}"
    llm = LocalDeterministicLLM()
    output = llm.complete_json(workflow, prompt, SCHEMAS[workflow])
    return {
        "workflow": workflow,
        "redactions": redactions,
        "retrieved_sources": sources,
        "structured_crm_update": output,
        "audit": {
            "human_approval_required": output["human_review_required"],
            "source_grounded": True,
            "raw_customer_data_sent": False,
        },
    }
