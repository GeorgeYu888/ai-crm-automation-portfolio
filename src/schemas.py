PROPOSAL_QA_SCHEMA = {
    "crm_record_type": "proposal_quality_review",
    "fields": ["summary", "missing_inputs", "compliance_flags", "recommended_next_actions", "human_review_required"],
}

SITE_SUMMARY_SCHEMA = {
    "crm_record_type": "site_assessment_summary",
    "fields": ["site_context", "constraints", "energy_opportunity", "follow_up_questions", "crm_notes"],
}

BILL_EXTRACT_SCHEMA = {
    "crm_record_type": "electricity_bill_extraction",
    "fields": ["customer", "nmi", "tariff", "usage_kwh", "demand_kw", "anomalies", "confidence"],
}

GHL_ONBOARDING_SCHEMA = {
    "crm_record_type": "gohighlevel_client_onboarding",
    "fields": [
        "client_goal",
        "pipeline_design",
        "tags",
        "triggers",
        "onboarding_tasks",
        "client_training_notes",
        "human_review_required",
    ],
}

ZAPIER_REPAIR_SCHEMA = {
    "crm_record_type": "automation_incident_review",
    "fields": [
        "broken_step",
        "likely_cause",
        "data_quality_checks",
        "safe_fix_plan",
        "rollback_plan",
        "client_update",
        "human_review_required",
    ],
}

EMAIL_FUNNEL_SCHEMA = {
    "crm_record_type": "landing_page_email_funnel",
    "fields": [
        "audience",
        "landing_page_sections",
        "email_sequence",
        "conversion_events",
        "tracking_plan",
        "approval_notes",
        "human_review_required",
    ],
}

DASHBOARD_SNAPSHOT_SCHEMA = {
    "crm_record_type": "performance_dashboard_snapshot",
    "fields": [
        "headline_metrics",
        "pipeline_risks",
        "automation_health",
        "client_follow_ups",
        "data_gaps",
        "human_review_required",
    ],
}
