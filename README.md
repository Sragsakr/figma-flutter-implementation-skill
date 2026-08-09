# Figma Flutter Implementation Skill

Converts a Figma screen to Flutter while respecting the active project's existing design system, assets, reusable widgets, structure, and UI state conventions.

The workflow is deliberately progressive: it verifies the checkout, inventories the live project and Figma, proves reuse before creating anything, implements only approved scope, then verifies the result.

## Install in Codex

Copy `codex/` to:

```text
~/.codex/skills/figma-flutter-implementation/
```

## Install in Claude Code

Copy `claude-code/` to:

```text
~/.claude/skills/figma-flutter-implementation/
```

Start a fresh Claude Code session, then invoke:

```text
/figma-flutter-implementation <Figma URL>
```

## Core guarantees

- Audit actual definitions and consumers before editing.
- Complete a per-component reuse inventory before creating any widget.
- Reuse the project's design tokens, assets accessors, widgets, state patterns, and responsive extensions.
- Do not add assets, dependencies, tokens, routes, shared components, or abstractions without explicit approval.
- Register approved assets through the project's asset source of truth; never use raw asset paths in UI code.
- Keep each screen's UI Cubit separate from independent business logic.
