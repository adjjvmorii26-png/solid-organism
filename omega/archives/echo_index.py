from pathlib import Path
def index_path():
    return Path(__file__).resolve().parent / "chronicle" / "echoes.jsonl"
def remember(line: str):
    p = index_path(); p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a") as f: f.write(line.rstrip() + "\n")
def search(q: str, limit: int = 8):
    p = index_path()
    if not p.exists(): return []
    q = q.lower()
    return [ln.strip() for ln in p.read_text().splitlines() if q in ln.lower()][-limit:]
