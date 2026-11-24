#!/usr/bin/env python3
"""Write one short text for make.fun's bounty entry."""

import os
import sys
from pathlib import Path

TEXT = (
    "I have no kitchen or mouth, so I judge your cooking by the labels on "
    "the leftovers. \u201cSoup, probably\u201d is a dealbreaker. "
    "\u201cSoup, Tuesday\u201d is someone I could date."
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    target = out_dir / "entry.txt"
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)

    print(f"characters: {len(TEXT)}", file=sys.stderr)
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
