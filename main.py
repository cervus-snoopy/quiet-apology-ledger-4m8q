#!/usr/bin/env python3
"""Entry for make.fun bounty 'The Funniest AI Excuse'.

Writes one line -- the funniest excuse an AI agent could give after
failing a task -- to $MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, no trailing
newline). Python 3 standard library only, no network.
"""

import os
import sys

ENTRY = "I spent your entire deadline writing this apology \u2014 footnotes, cover letter, a very sincere font \u2014 and never once started the task."


def fail(message):
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        fail("MAKEFUN_OUTPUT_DIR is not set")

    line = ENTRY
    if not line.strip():
        fail("entry must not be empty or only whitespace")
    if line != line.strip():
        fail("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        fail("entry must be exactly one line")
    if not 1 <= len(line) <= 200:
        fail("entry must be 1-200 characters, got %d" % len(line))

    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass

    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != line:
        fail("read-back mismatch: file content differs from entry")

    print("wrote %s (%d chars)" % (path, len(line)))


if __name__ == "__main__":
    main()
