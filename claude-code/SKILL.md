---
name: figma-flutter-implementation
description: Convert a Figma frame or design URL into maintainable Flutter UI while preserving the target project's active theme, design system, reusable widgets, feature structure, assets, and state-management conventions. Use for Figma-to-Flutter implementation, sync, or visual refinement where DRY rules and strict no-unapproved-additions discipline are required.
---

# Figma to Flutter Implementation

Treat the Figma URL as the visual source and the current project source as the implementation source of truth. Follow phases in order. Do not skip a gate or load a later reference early.

## Phase 0 — Scope And Baseline Gate

Before reading Figma or code, load [discovery.md](references/discovery.md). Confirm the current checkout and branch. Use that checkout by default. Never create or use another branch or worktree unless the user explicitly requests it.

## Phase 1 — Evidence Gate

Load [discovery.md](references/discovery.md). Use the installed Figma design-to-code skill and Figma MCP before requesting design context. Inspect Figma plus active project source and publish the required inventory before editing.

## Phase 2 — Reuse Gate

Load [reuse-rules.md](references/reuse-rules.md). Map every Figma color, type style, spacing value, radius, shadow, asset, and component to an existing project item. If the screen needs an image or icon, load [assets.md](references/assets.md) before exporting, downloading, registering, or using it.

If a required capability is absent, report the precise gap and wait for explicit user approval. Never create an unapproved token, file, route, shared component, dependency, asset, abstraction, or feature boundary.

## Phase 3 — Screen Implementation

Load [screen-architecture.md](references/screen-architecture.md) only after the first two gates. Implement only the user-authorized screen scope using verified project patterns.

## Phase 4 — Verification And Handoff

Load [verification.md](references/verification.md) after implementation. Verify targeted behavior, visual fidelity, and scope. Report evidence, reused items, changed files, and unresolved gaps.

## Always-On Guardrails

- Preserve DRY: never duplicate tokens, widgets, dialogs, or business logic.
- Prefer existing semantic project systems over literal copying from Figma.
- Do not redesign unrelated UI, refactor unrelated code, or make changes for an analysis-only request.
