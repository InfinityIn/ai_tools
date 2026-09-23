"""Tests for scripts/day0_check.py.

The script is exercised through subprocess on the real call site
(``python scripts/day0_check.py``), not only by importing a function:
the default-path resolution and the exit code are part of the contract.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = PROJECT_ROOT / "scripts" / "day0_check.py"
DAY0 = PROJECT_ROOT / "DAY0.md"

# Every regulation marked "day 0" in the ai_tools catalogue.
# Changing the checklist must break this test on purpose.
EXPECTED_OPEN_ITEMS = 29


def run(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=str(cwd) if cwd is not None else None,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )


def open_count(output: str) -> int:
    match = re.search(r"^(\d+) open items$", output, re.MULTILINE)
    assert match is not None, f"no summary line in output:\n{output}"
    return int(match.group(1))


def test_template_checklist_is_fully_open(tmp_path: Path) -> None:
    """The shipped template must fail the gate: nothing is done yet."""
    result = run(cwd=tmp_path)  # no argument -> default path next to scripts/
    assert result.returncode == 1, result.stdout + result.stderr
    assert open_count(result.stdout) == EXPECTED_OPEN_ITEMS
    # every open item is printed, not just counted
    for code in ("R0.1", "R2.3", "R3.4", "R7.5"):
        assert code in result.stdout


def test_explicit_path_argument(tmp_path: Path) -> None:
    result = run(str(DAY0), cwd=tmp_path)
    assert result.returncode == 1
    assert open_count(result.stdout) == EXPECTED_OPEN_ITEMS


def test_all_checked_passes(tmp_path: Path) -> None:
    copy = tmp_path / "DAY0.md"
    copy.write_text(
        DAY0.read_text(encoding="utf-8").replace("- [ ] R", "- [x] R"),
        encoding="utf-8",
    )
    result = run(str(copy))
    assert result.returncode == 0, result.stdout + result.stderr
    assert "0 open items" not in result.stdout
    assert f"all {EXPECTED_OPEN_ITEMS} items closed" in result.stdout


def test_uppercase_checkbox_counts_as_closed(tmp_path: Path) -> None:
    copy = tmp_path / "DAY0.md"
    copy.write_text(
        DAY0.read_text(encoding="utf-8").replace("- [ ] R", "- [X] R"),
        encoding="utf-8",
    )
    result = run(str(copy))
    assert result.returncode == 0, result.stdout + result.stderr


def _one_item_project(tmp_path: Path, line: str) -> Path:
    day0 = tmp_path / "DAY0.md"
    day0.write_text(
        "# Day 0\n\nsome prose that is not a checkbox\n\n" + line + "\n",
        encoding="utf-8",
    )
    return day0


def test_skip_without_adr_stays_open(tmp_path: Path) -> None:
    day0 = _one_item_project(
        tmp_path, "- [ ] R6.5 - backup and restore test [skip: ADR-0002]"
    )
    result = run(str(day0))
    assert result.returncode == 1, result.stdout
    assert "skip without ADR" in result.stdout
    assert open_count(result.stdout) == 1


def test_skip_with_adr_is_closed(tmp_path: Path) -> None:
    day0 = _one_item_project(
        tmp_path, "- [ ] R6.5 - backup and restore test [skip: ADR-0002]"
    )
    adr = tmp_path / "docs" / "adr"
    adr.mkdir(parents=True)
    (adr / "0002-no-backup-yet.md").write_text("# ADR-0002\n", encoding="utf-8")
    result = run(str(day0))
    assert result.returncode == 0, result.stdout + result.stderr
    assert "all 1 items closed" in result.stdout


def test_non_checkbox_lines_are_ignored(tmp_path: Path) -> None:
    day0 = tmp_path / "DAY0.md"
    day0.write_text(
        "# Day 0\n\n"
        "- a plain bullet\n"
        "  `- [ ] R9.9 - example inside prose`\n"
        "- [x] R0.1 - constitution\n",
        encoding="utf-8",
    )
    result = run(str(day0))
    assert result.returncode == 0, result.stdout + result.stderr
    assert "all 1 items closed" in result.stdout


def test_fenced_examples_are_not_checklist_items(tmp_path: Path) -> None:
    day0 = tmp_path / "DAY0.md"
    day0.write_text(
        "# Day 0\n\n"
        "```\n"
        "- [ ] R9.9 - an example of the skip syntax [skip: ADR-0002]\n"
        "```\n\n"
        "- [x] R0.1 - constitution\n",
        encoding="utf-8",
    )
    result = run(str(day0))
    assert result.returncode == 0, result.stdout + result.stderr
    assert "R9.9" not in result.stdout
    assert "all 1 items closed" in result.stdout


def test_missing_file_is_an_error(tmp_path: Path) -> None:
    result = run(str(tmp_path / "nope.md"))
    assert result.returncode == 2
    assert "not found" in (result.stdout + result.stderr)


def test_template_checklist_matches_the_file(tmp_path: Path) -> None:
    """Guard against the script silently parsing nothing."""
    raw = DAY0.read_text(encoding="utf-8")
    in_file = len(re.findall(r"^- \[ \] R", raw, re.MULTILINE))
    assert in_file == EXPECTED_OPEN_ITEMS
    shutil.copy(DAY0, tmp_path / "DAY0.md")
    assert open_count(run(str(tmp_path / "DAY0.md")).stdout) == in_file


def test_shipped_adr_dir_claims_no_number(tmp_path: Path) -> None:
    """The ADR template must not occupy a number a skip could point at.

    A file named 0001-*.md would let a fresh project waive its first
    checklist item with [skip: ADR-0001] - pointing at an empty template.
    """
    shutil.copytree(PROJECT_ROOT / "docs" / "adr", tmp_path / "docs" / "adr")
    day0 = _one_item_project(tmp_path, "- [ ] R0.1 - constitution [skip: ADR-0001]")
    result = run(str(day0))
    assert result.returncode == 1, result.stdout + result.stderr
    assert "skip without ADR" in result.stdout


def test_file_without_checkboxes_is_an_error(tmp_path: Path) -> None:
    """A checklist the parser cannot read is a failure, not a pass."""
    day0 = tmp_path / "DAY0.md"
    day0.write_text("# Day 0\n\nprose only, no checkboxes at all\n", encoding="utf-8")
    result = run(str(day0))
    assert result.returncode == 2, result.stdout + result.stderr
    assert "no checklist items" in (result.stdout + result.stderr)


def test_adr_with_another_number_does_not_close_skip(tmp_path: Path) -> None:
    """Any ADR is not enough: it must be the one the skip names."""
    day0 = _one_item_project(
        tmp_path, "- [ ] R6.5 - backup and restore test [skip: ADR-0002]"
    )
    adr = tmp_path / "docs" / "adr"
    adr.mkdir(parents=True)
    (adr / "0003-something-else.md").write_text("# ADR-0003\n", encoding="utf-8")
    result = run(str(day0))
    assert result.returncode == 1, result.stdout + result.stderr
    assert "skip without ADR" in result.stdout
    assert open_count(result.stdout) == 1


def test_malformed_skip_is_not_a_skip(tmp_path: Path) -> None:
    """[skip: we will write it later] is a plain open item, not a waiver."""
    day0 = _one_item_project(
        tmp_path, "- [ ] R6.5 - backup and restore test [skip: потом напишем]"
    )
    result = run(str(day0))
    assert result.returncode == 1, result.stdout + result.stderr
    assert open_count(result.stdout) == 1
    # not even recognised as an attempted skip
    assert "skip without ADR" not in result.stdout


def test_skip_token_does_not_leak_into_the_printed_title(tmp_path: Path) -> None:
    day0 = tmp_path / "DAY0.md"
    day0.write_text(
        "# Day 0\n\n"
        "- [ ] R6.5 - backup and restore test [skip: ADR-0002]\n"
        "- [ ] R6.1 - slo and alerts [skip: потом напишем]\n",
        encoding="utf-8",
    )
    result = run(str(day0))
    assert result.returncode == 1, result.stdout + result.stderr
    for line in result.stdout.splitlines():
        if line.lstrip().startswith("[ ]"):
            assert "[skip:" not in line, line
