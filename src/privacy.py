from __future__ import annotations

import re


EMAIL_RE = re.compile(r"[\w\.-]+@[\w\.-]+\.\w+")
PHONE_RE = re.compile(r"(\+?61|0)[2-478](?:[ -]?\d){8}")
NMI_RE = re.compile(r"\b\d{10,11}\b")


def redact_sensitive_text(text: str) -> tuple[str, list[str]]:
    findings: list[str] = []
    redacted = EMAIL_RE.sub("[REDACTED_EMAIL]", text)
    if redacted != text:
        findings.append("email")
    text = redacted
    redacted = PHONE_RE.sub("[REDACTED_PHONE]", text)
    if redacted != text:
        findings.append("phone")
    text = redacted
    redacted = NMI_RE.sub("[REDACTED_NMI]", text)
    if redacted != text:
        findings.append("nmi")
    return redacted, sorted(set(findings))
