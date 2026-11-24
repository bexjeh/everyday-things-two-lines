#!/usr/bin/env python3
"""Everyday Things, Two Lines: a sponge, explained to a 10-year-old.

Deterministic: no clock, no environment input beyond the output directory,
no randomness. Writes exactly two lines to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to the current directory when the variable is unset).
"""
import os
from pathlib import Path

LINES = [
    "A sponge is a city of tiny empty rooms, and every room drinks one drop of water and holds it until you squeeze.",
    "The rooms map the holes soaking up water and letting it go when squeezed, but they leave out that nothing inside is alive - a sponge never chooses to drink, it only fills.",
]


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    path = Path(out_dir) / "entry.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(LINES) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
