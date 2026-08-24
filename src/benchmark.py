from __future__ import annotations


def score_model(name: str, accuracy: float, latency_ms: int, cost_usd: float) -> dict:
    value_score = accuracy * 100 - latency_ms / 1000 - cost_usd * 10
    return {
        "model": name,
        "accuracy": accuracy,
        "latency_ms": latency_ms,
        "estimated_cost_usd": cost_usd,
        "value_score": round(value_score, 2),
    }
