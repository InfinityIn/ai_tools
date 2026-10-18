#!/usr/bin/env python3
"""Check vendored design payloads against their pinned, LF-normalized hashes."""
import argparse
import hashlib
import json
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def check(root, installed=None):
    manifest = json.loads((root / "data/design-skills.lock.json").read_text(encoding="utf-8"))
    errors = []
    count = 0
    for skill in manifest["skills"]:
        folder = installed / skill["name"] if installed else root / skill["destination"]
        expected = {item["path"] for item in skill["files"]}
        actual = {p.relative_to(folder).as_posix() for p in folder.rglob("*") if p.is_file()}
        for missing in sorted(expected - actual):
            errors.append(f"MISSING {skill['name']}/{missing}")
        for extra in sorted(actual - expected):
            errors.append(f"EXTRA {skill['name']}/{extra}")
        for item in skill["files"]:
            path = folder / item["path"]
            if path.is_file() and digest(path) != item["sha256"]:
                errors.append(f"DIFFERS {skill['name']}/{item['path']}")
            count += 1
    process = root / "src/process/design-it"
    for relative in ("SKILL.md", "references/acceptance.md"):
        source = process / relative
        if not source.is_file():
            errors.append(f"MISSING design-it/{relative}")
        elif installed:
            target = installed / "design-it" / relative
            if not target.is_file() or digest(target) != digest(source):
                errors.append(f"DIFFERS installed design-it/{relative}")
    base = installed / "orchestrate/SKILL.md" if installed else root / "src/process/orchestrate/SKILL.md"
    if not base.is_file():
        errors.append("MISSING orchestrate dependency")
    for error in errors:
        print(error)
    print(f"{'FAIL' if errors else 'OK'}: 5 upstream skills, {count} pinned files, design-it and orchestrate")
    return 1 if errors else 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--installed", type=Path, help="Check an installed skill directory instead of src")
    args = parser.parse_args()
    raise SystemExit(check(Path(__file__).resolve().parents[1], args.installed))
