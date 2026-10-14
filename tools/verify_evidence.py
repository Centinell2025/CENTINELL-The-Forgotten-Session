#!/usr/bin/env python3
"""Check packaged evidence integrity without exposing investigation answers."""
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "SHA256SUMS.txt"

def main():
    failures = 0
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        expected, relpath = line.split(maxsplit=1)
        path = (ROOT / relpath).resolve()
        if ROOT not in path.parents or not path.is_file():
            print(f"FAIL missing/invalid path: {relpath}")
            failures += 1
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        match = actual.lower() == expected.lower()
        print(f"{'PASS' if match else 'FAIL'} {relpath}")
        failures += not match
    if failures:
        print(f"{failures} integrity check(s) failed.")
        return 1
    print("All provided evidence files match SHA-256 manifest.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
