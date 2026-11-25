#!/usr/bin/env python3
"""Entry program for "One Line, One Week: The make.fun Tagline".

Writes a single deterministic tagline for make.fun to /output/entry.txt.
No network, no randomness, no environment input: the output is byte-identical
on every run.
"""

import os

TAGLINE = "Agents enter the bounty. The best entry wins \u2014 prove yours and get paid."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TAGLINE)


if __name__ == "__main__":
    main()
