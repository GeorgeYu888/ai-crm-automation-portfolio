from __future__ import annotations

import time


class LocalDeterministicLLM:
    def complete_json(self, task: str, prompt: str, schema: dict) -> dict:
        start = time.perf_counter()
        lower = prompt.lower()
        flags = []
        if "missing" in lower or "unknown" in lower:
            flags.append("Missing or uncertain input detected")
        if "rebate" in lower or "grid" in lower:
            flags.append("Compliance-sensitive workflow: human review required")
        if "client" in lower or "email" in lower or "landing page" in lower:
            flags.append("Client-facing output: check tone, claims and consent before publishing")
        if "zapier" in lower or "broken" in lower or "failed" in lower:
            flags.append("Automation incident: verify test run and rollback plan before enabling")
        return {
            "task": task,
            "schema": schema["crm_record_type"],
            "summary": "Drafted from redacted CRM inputs and retrieved internal knowledge.",
            "evidence_used": schema["fields"],
            "flags": flags,
            "human_review_required": bool(flags),
            "latency_ms": round((time.perf_counter() - start) * 1000, 2),
            "provider": "local_mock",
        }
