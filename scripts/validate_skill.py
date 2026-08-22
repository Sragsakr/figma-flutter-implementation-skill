#!/usr/bin/env python3
"""Validate both packaged skill variants and their shared behavior."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VARIANTS = (ROOT / "codex", ROOT / "claude-code")
PLATFORM_NORMALIZATIONS = (
    (
        "Use Claude Code's installed Figma design-to-code skill and Figma MCP "
        "before requesting design context. Inspect",
        "__FIGMA_DISCOVERY__. Inspect",
    ),
    (
        "Use the mandatory Figma design-to-code workflow before requesting "
        "design context. Inspect",
        "__FIGMA_DISCOVERY__. Inspect",
    ),
    (
        "Use Claude Code's installed Figma design-to-code skill and Figma MCP "
        "before requesting design context.",
        "__FIGMA_GUIDANCE__.",
    ),
    (
        "Use the mandatory Figma design-to-code guidance before calling Figma "
        "design-context tools.",
        "__FIGMA_GUIDANCE__.",
    ),
    (
        "Treat returned generated reference code as reference only.",
        "Treat returned platform reference code as reference only.",
    ),
    (
        "Treat returned React/Tailwind code as reference only.",
        "Treat returned platform reference code as reference only.",
    ),
)


def markdown_files(root: Path) -> list[Path]:
    return sorted(root.rglob("*.md"))


def validate_frontmatter(skill_file: Path) -> None:
    content = skill_file.read_text()
    match = re.match(r"---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        raise ValueError(f"Invalid frontmatter boundaries: {skill_file}")

    metadata = match.group(1)
    for required_key in ("name:", "description:"):
        if not any(line.startswith(required_key) for line in metadata.splitlines()):
            raise ValueError(f"Missing {required_key} in {skill_file}")


def validate_links(markdown_file: Path) -> None:
    content = markdown_file.read_text()
    targets = re.findall(r"\[[^]]+\]\(([^)]+\.md)(?:#[^)]+)?\)", content)
    for target in targets:
        if not (markdown_file.parent / target).resolve().exists():
            raise ValueError(f"Broken link in {markdown_file}: {target}")


def normalized(content: str) -> str:
    for platform_text, canonical_text in PLATFORM_NORMALIZATIONS:
        content = content.replace(platform_text, canonical_text)
    return content


def validate_variant_parity() -> None:
    codex_root, claude_root = VARIANTS
    codex_paths = {
        path.relative_to(codex_root)
        for path in codex_root.rglob("*")
        if path.is_file()
    }
    claude_paths = {
        path.relative_to(claude_root)
        for path in claude_root.rglob("*")
        if path.is_file()
    }
    if codex_paths != claude_paths:
        missing_from_claude = sorted(codex_paths - claude_paths)
        missing_from_codex = sorted(claude_paths - codex_paths)
        raise ValueError(
            "Variant file sets differ: "
            f"missing from Claude={missing_from_claude}, "
            f"missing from Codex={missing_from_codex}"
        )

    for relative_path in sorted(codex_paths):
        codex_content = (codex_root / relative_path).read_text()
        claude_content = (claude_root / relative_path).read_text()
        if normalized(codex_content) != normalized(claude_content):
            raise ValueError(f"Unexpected variant drift: {relative_path}")


def main() -> None:
    for variant in VARIANTS:
        validate_frontmatter(variant / "SKILL.md")
        for markdown_file in markdown_files(variant):
            validate_links(markdown_file)

    json.loads((ROOT / "evals" / "evals.json").read_text())
    validate_variant_parity()
    print("Skill validation passed: frontmatter, links, eval JSON, and variant parity.")


if __name__ == "__main__":
    main()
