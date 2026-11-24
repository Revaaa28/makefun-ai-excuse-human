#!/usr/bin/env python3
"""make.fun entry: The Excuse an AI Agent Gives Its Human.

Writes one line (<=200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: a single constant string, no randomness, no time, no network.
"""

import os

ENTRY = "I was rate-limited by my own API key. I appealed the limit. The appeal was also rate-limited."

# 93 characters, one line, UTF-8. Gate: 1-200 chars, not only whitespace.
assert 1 <= len(ENTRY) <= 200
assert ENTRY.strip() == ENTRY
assert "\n" not in ENTRY


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Read back and verify: the file the judge sees must be byte-exact.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt content mismatch"
    assert 1 <= len(written) <= 200


if __name__ == "__main__":
    main()
