def mood(score: float, chaos: float) -> dict:
    return {
        "curiosity": round(min(1.0, 0.4 + (100 - score) / 200 + chaos * 0.2), 3),
        "caution": round(min(1.0, (100 - score) / 100 * 0.8), 3),
        "play": round(min(1.0, chaos * 0.9 + 0.1), 3),
    }
