#!/usr/bin/env python3
"""The 3AM Fridge Text.

Writes the one line a smart fridge texts its owner at 3am to
/output/entry.txt. Stdlib only; deterministic; no network, no input.
"""

import os

LINE = "It's 3am. You're looking for something. I've watched you look for 4 years. It's not in here. It was never in here."


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
