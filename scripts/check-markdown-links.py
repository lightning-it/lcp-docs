#!/usr/bin/env python3
"""Fail when a repository-local Markdown link points to a missing target."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+['\"][^'\"]+['\"])?\)")
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel"}


def target_exists(source: Path, raw_target: str) -> bool:
    parsed = urlsplit(raw_target)
    if parsed.scheme.lower() in EXTERNAL_SCHEMES or raw_target.startswith("#"):
        return True
    if parsed.scheme or parsed.netloc:
        return False
    target = unquote(parsed.path)
    if not target:
        return True
    resolved = (source.parent / target).resolve()
    try:
        resolved.relative_to(ROOT)
    except ValueError:
        return False
    return resolved.exists()


def main() -> int:
    failures: list[str] = []
    for source in sorted(ROOT.rglob("*.md")):
        if ".git" in source.parts:
            continue
        for line_number, line in enumerate(
            source.read_text(encoding="utf-8").splitlines(), start=1
        ):
            for match in LINK.finditer(line):
                target = match.group(1)
                if not target_exists(source, target):
                    failures.append(
                        f"{source.relative_to(ROOT)}:{line_number}: missing link target {target}"
                    )
    if failures:
        print("\n".join(failures))
        return 1
    print("All repository-local Markdown links resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
