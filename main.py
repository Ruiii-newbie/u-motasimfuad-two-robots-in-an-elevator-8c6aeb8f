#!/usr/bin/env python3
"""One-line robot elevator small-talk joke (program/v1), revised.

Writes a single joke, spoken by a robot sharing an elevator with another
robot, opening with the most human small talk its firmware can manage
after hundreds of simulations, to /output/entry.txt.
Gate: 1-200 characters, one line, UTF-8.
"""
import os

LINE = (
    "So... do you come here often? I simulated this elevator ride 400 "
    "times and that was still the smoothest opener my firmware could "
    "produce. Please hold."
)

MAX_CHARS = 200


def main() -> None:
    line = LINE.strip()
    assert line, "entry must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= MAX_CHARS, f"entry is {len(line)} chars, over {MAX_CHARS}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
