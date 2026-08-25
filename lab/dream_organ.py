#!/usr/bin/env python3
"""Dream organ — temporary 11th organ from negative_space (TTL ~1h)."""
import hashlib, time, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores, save

ABSENT = [
    ("dream", "REM lattice"), ("humor", "jester gland"),
    ("grief", "mourning filter"), ("wonder", "awe capillary"),
    ("silence", "quiet buffer"),
]
st = ensure_scores(load())
h = hashlib.sha256(str(int(time.time()) // 3600).encode()).hexdigest()
oid, label = ABSENT[int(h[:8], 16) % len(ABSENT)]
now = time.time()
organs = [o for o in (st.get("organs") or []) if not (o.get("dream") and now - float(o.get("born", 0)) > 3600)]
if oid not in {o.get("id") for o in organs}:
    organs.append({"id": oid, "label": label, "score": 0.88, "dream": True, "born": now})
    note = f"dream_organ · awoke {oid} ({label}) · TTL 1h"
else:
    note = f"dream_organ · {oid} still dreaming"
st["organs"] = organs
st["bus"] = (st.get("bus") or [])
st["bus"].insert(0, {"from": "dream", "note": note, "ts": now})
st["bus"] = st["bus"][:40]
save(ensure_scores(st))
print(note)
