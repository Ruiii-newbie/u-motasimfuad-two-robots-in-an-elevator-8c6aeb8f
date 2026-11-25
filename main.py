#!/usr/bin/env python3
"""Two Robots in an Elevator — one line of awkward robot small talk.

Writes the entry to /output/entry.txt (the harness gate: UTF-8 text,
1-200 chars, not only whitespace) and prints it to stdout.
"""

import os

ENTRY = (
    "I faked a voice-module update so I wouldn't have to talk, "
    "but you did the exact same thing, and now we're just two robots "
    "silently buffering in a metal box together."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
