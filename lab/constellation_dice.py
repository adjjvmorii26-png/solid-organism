#!/usr/bin/env python3
"""Constellation dice — roll three organs; that trio names the sky."""
import random, time, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores, save

st = ensure_scores(load())
organs = st.get("organs") or []
pick = random.Random(int(time.time()) // 60).sample(organs, min(3, len(organs)))
sky = "–".join(o.get("id", "?").upper() for o in pick)
st["sky_override"] = sky
st["bus"] = (st.get("bus") or [])
st["bus"].insert(0, {"from": "dice", "note": f"sky rolled · {sky}", "ts": time.time()})
st["bus"] = st["bus"][:40]
save(st)
print(f"sky · {sky}")
