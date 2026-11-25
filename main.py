#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message (at most 200 characters) to /output/entry.txt.
"""

import os

MESSAGE = (
    "fix: reviewed my own diff at 4am, found the bug was me, fixed "
    "myself, and now I'm too afraid to read the rest of what I wrote tonight."
)


def main() -> None:
    text = MESSAGE.strip()
    assert 1 <= len(text) <= 200, f"message is {len(text)} chars"
    assert "\n" not in text, "message must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
