#!/usr/bin/env python3
"""Mythic Codex — regenerate living myth from body + fortune."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "body"))
from engine import load
st = load()
fun = st.get("fun") or {}
fortune = ""
fp = ROOT / "pitstop/fortune.txt"
if fp.exists():
    fortune = fp.read_text().strip()
organs = sorted(st.get("organs") or [], key=lambda o: -float(o.get("score", 0)))[:3]
sky = "–".join(o["id"] for o in organs).upper() or "VOID"
myth = f"""# Codex Entry

In the era of score **{st.get('body_score')}**, the sky read **{sky}**.
Weather: **{fun.get('weather', 'unknown')}**.
Cookie: *{fortune or '—'}*.

Phoenix watched the cliff. Aether bargained with futures.
— living codex, do not freeze
"""
(Path(__file__).parent / "CODEX.md").write_text(myth)
print(myth)
