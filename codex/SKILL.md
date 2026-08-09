---
name: figma-flutter-implementation
description: Convert a Figma frame or design URL into maintainable Flutter UI while preserving the target project's active theme, design system, reusable widgets, feature structure, and state-management conventions. Use for Figma-to-Flutter implementation, sync, or visual refinement where DRY rules and strict no-unapproved-additions discipline are required.
---

# Figma to Flutter Implementation

Treat the Figma URL as the visual source and the current project source as the implementation source of truth. Follow phases in order. Do not skip a gate or load a later reference early.

## Phase 0 — Scope And Baseline Gate

Before reading Figma or code, load [discovery.md](references/discovery.md).

Confirm the target checkout and branch. Use the user's current checkout by default. Never create or use another branch or worktree unless the user explicitly requests it. If the baseline cannot be verified, stop and ask one concise question.

## Phase 1 — Evidence Gate

Load [discovery.md](references/discovery.md) and inspect Figma plus the active project source. Complete the required inventory before editing. Treat actual definitions and their call sites as authoritative; never infer absence from a sparse directory or missing filename.

Publish a concise inventory of the existing system, components, shell, state-management patterns, and Figma mapping. Do not edit code before this inventory exists.

## Phase 2 — Reuse Gate

Load [reuse-rules.md](references/reuse-rules.md). Map every Figma color, type style, spacing value, radius, shadow, asset, and component to an existing project item before implementing.

If a required capability is absent, report the precise gap and wait for explicit user approval. Never create an unapproved token, file, route, shared component, dependency, asset, abstraction, or feature boundary.

If the screen needs an image or icon, load [assets.md](references/assets.md) before exporting, downloading, registering, or using an asset.

## Phase 3 — Screen Implementation

Load [screen-architecture.md](references/screen-architecture.md) only after passing the first two gates. Implement only the user-authorized screen scope using the verified project patterns.

## Phase 4 — Verification And Handoff

Load [verification.md](references/verification.md) after implementation. Verify the targeted behavior, visual fidelity, and scope. Report evidence, reused items, changed files, and unresolved gaps.

## Always-On Guardrails

- Preserve DRY: never duplicate tokens, widgets, dialogs, or business logic.
- Prefer existing semantic project systems over literal copying from Figma.
- Do not redesign unrelated UI, refactor unrelated code, or make changes for an analysis-only request.
- Use the mandatory Figma design-to-code guidance before calling Figma design context tools.
