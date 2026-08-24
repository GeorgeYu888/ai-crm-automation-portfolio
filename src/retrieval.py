from __future__ import annotations

import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = ROOT / "data" / "knowledge"


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z0-9]{3,}", text.lower()))


def retrieve(query: str, limit: int = 3) -> list[dict]:
    q = tokenize(query)
    scored = []
    for path in KNOWLEDGE_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        tokens = tokenize(text)
        overlap = len(q & tokens)
        score = overlap / math.sqrt(max(len(tokens), 1))
        scored.append({"source": path.name, "score": round(score, 4), "excerpt": text[:650]})
    return sorted(scored, key=lambda row: row["score"], reverse=True)[:limit]
