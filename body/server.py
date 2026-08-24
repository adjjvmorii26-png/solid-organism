#!/usr/bin/env python3
"""Minimal body HTTP console."""
from __future__ import annotations
import json, argparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from engine import load, save, ensure_scores, run_pulse, integration_checks, body_score

class H(BaseHTTPRequestHandler):
    def _json(self, code, obj):
        b = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)
    def do_GET(self):
        try:
            st = ensure_scores(load())
        except Exception as e:
            return self._json(500, {"error": str(e)})
        if self.path.startswith("/api/status") or self.path.startswith("/api/body"):
            return self._json(200, {
                "score": body_score(st),
                "version": st.get("version"),
                "agents": len(st.get("agents") or []),
                "integ": integration_checks(st),
            })
        if self.path.startswith("/api/bus"):
            return self._json(200, {"bus": (st.get("bus") or [])[:20]})
        return self._json(404, {"error": "not found"})
    def do_POST(self):
        if self.path.startswith("/api/pulse"):
            st = ensure_scores(load())
            st = run_pulse(st)
            save(st)
            return self._json(200, {"score": body_score(st), "ok": True})
        return self._json(404, {"error": "not found"})
    def log_message(self, *a):
        pass

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8890)
    args = ap.parse_args()
    print(f"body · http://127.0.0.1:{args.port}/")
    HTTPServer(("127.0.0.1", args.port), H).serve_forever()

if __name__ == "__main__":
    main()
