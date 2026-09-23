#!/usr/bin/env python3
"""Fail while DAY0.md still has open items.

Day 0 is not a document, it is a gate: this script is a step of the
unconditional CI job (R4.2) and keeps the build red until every checklist
item is either done (``- [x]``) or consciously waived with an ADR that
really exists (``[skip: ADR-nnnn]``).

Usage:
    python scripts/day0_check.py [PATH_TO_DAY0_MD]

Default path: DAY0.md next to the scripts/ directory (the project root).
Exit codes: 0 - everything closed, 1 - open items left, 2 - bad input.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import NamedTuple

CHECKBOX = re.compile(r"^\s*- \[(?P<mark>[ xX])\]\s+(?P<body>.+?)\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
SKIP = re.compile(r"\[skip:\s*ADR-(?P<number>\d{4})\]")
CODE = re.compile(r"^(?P<code>R\d+\.\d+)")
SEPARATORS = (" — ", " - ")


class Item(NamedTuple):
    """One checklist line."""

    code: str
    title: str
    reason: str  # "" when the item is closed


def parse_item(body: str, checked: bool, project_root: Path) -> Item | None:
    """Turn one checkbox line into an Item, or None if it has no R-code."""
    code_match = CODE.match(body)
    if code_match is None:
        return None
    code = code_match.group("code")
    title = title_of(body[len(code) :])
    if checked:
        return Item(code, title, "")
    skip = SKIP.search(body)
    if skip is None:
        return Item(code, title, "open")
    if adr_exists(project_root, skip.group("number")):
        return Item(code, title, "")
    return Item(code, title, f"skip without ADR (docs/adr/{skip.group('number')}-*.md)")


def title_of(tail: str) -> str:
    """The human-readable name of the item: the field after the code."""
    for separator in SEPARATORS:
        if tail.startswith(separator):
            rest = tail[len(separator) :]
            for end in SEPARATORS:
                if end in rest:
                    return rest.split(end, 1)[0].strip()
            return SKIP.sub("", rest).strip()
    return SKIP.sub("", tail).strip()


def adr_exists(project_root: Path, number: str) -> bool:
    return any((project_root / "docs" / "adr").glob(f"{number}-*.md"))


def collect(day0: Path) -> list[Item]:
    project_root = day0.resolve().parent
    items: list[Item] = []
    inside_fence = False
    for line in day0.read_text(encoding="utf-8").splitlines():
        if FENCE.match(line):
            # examples inside ``` blocks are documentation, not the checklist
            inside_fence = not inside_fence
            continue
        if inside_fence:
            continue
        match = CHECKBOX.match(line)
        if match is None:
            continue
        item = parse_item(
            match.group("body"), match.group("mark") != " ", project_root
        )
        if item is not None:
            items.append(item)
    return items


def default_day0() -> Path:
    return Path(__file__).resolve().parent.parent / "DAY0.md"


def force_utf8() -> None:
    """Print UTF-8 regardless of the console code page (Windows: cp1251)."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8", errors="replace")


def main(argv: list[str]) -> int:
    force_utf8()
    day0 = Path(argv[0]) if argv else default_day0()
    if not day0.is_file():
        print(f"day0_check: {day0} not found", file=sys.stderr)
        return 2

    items = collect(day0)
    if not items:
        print(f"day0_check: no checklist items found in {day0}", file=sys.stderr)
        return 2

    open_items = [item for item in items if item.reason]
    for item in open_items:
        suffix = "" if item.reason == "open" else f"  <- {item.reason}"
        print(f"  [ ] {item.code} - {item.title}{suffix}")

    print(f"{len(items)} items total")
    if open_items:
        print(f"{len(open_items)} open items")
        return 1
    print(f"all {len(items)} items closed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
