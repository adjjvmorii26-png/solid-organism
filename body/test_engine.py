#!/usr/bin/env python3
"""Smoke test body engine."""
from engine import load, ensure_scores, integration_checks, body_score
st = ensure_scores(load())
ic = integration_checks(st)
print("score", body_score(st))
print("integ", ic.get("passed"), "/", ic.get("total"))
assert ic.get("passed", 0) >= 1
print("ok")
