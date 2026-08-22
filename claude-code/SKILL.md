---
name: figma-flutter-implementation
description: Create, update, synchronize, or visually refine Flutter screens and flows from Figma while preserving the target project's active theme, design system, reusable widgets, feature structure, assets, routing, and state-management conventions. Use for new Figma-to-Flutter implementation and for reconciling an existing Flutter UI after its Figma design adds, removes, or changes elements. Requires an evidence-backed build/change contract before editing and strict control of unapproved or speculative additions.
---

# Figma to Flutter Implementation

Treat Figma as the visual target and the active project as the implementation source of truth. Preserve the proven reuse-first creation behavior while making every planned addition, modification, and removal reviewable before code changes.

Follow the phases in order. Load a reference when its phase requires it; do not edit before the contract gate passes.

## Phase 0 — Scope And Mode Gate

Load [discovery.md](references/discovery.md).

Verify the current checkout and branch, identify the exact Figma and project scope, then classify the request as:

- `CREATE`: the authorized screen or flow is not implemented.
- `SYNC`: an implementation exists and must be reconciled with a changed Figma target.
- `REFINE`: a bounded visual or component-level adjustment to an existing implementation.
- `ANALYZE`: inventory and plan only; never edit.

Use the user's current checkout by default. Never create or use another branch or worktree unless explicitly requested. If the target or scope completeness cannot be verified, ask one concise question before continuing.

## Phase 1 — Evidence Gate

Complete the Figma and project inventories in [discovery.md](references/discovery.md). Treat definitions plus real consumers as authoritative. Do not infer absence from a guessed filename, sparse directory, inaccessible Figma node, or partial frame.

For `SYNC` and `REFINE`, capture the current implementation baseline and load [change-reconciliation.md](references/change-reconciliation.md). For `CREATE`, load [create-workflow.md](references/create-workflow.md).

## Phase 2 — Implementation Contract Gate

Load [implementation-contract.md](references/implementation-contract.md), then publish the required contract before editing:

- Scope and explicit exclusions.
- Evidence-backed build tree for `CREATE`, or change tree for `SYNC`/`REFINE`.
- Action table, affected files, reuse decisions, additions, destructive changes, blocked gaps, and verification plan.
- For `CREATE`: Figma coverage, behavior/data sources, state coverage, and architecture budget.
- For `SYNC`/`REFINE`: current-to-target differences and separate decisions for UI usage, source files, assets, state, navigation, and business logic.

Wait for one approval covering the complete contract. Approved listed changes need no repeated approval. If implementation reveals an unlisted change, publish a focused Plan Delta and wait only for that delta. In `ANALYZE`, stop after the contract.

## Phase 3 — Reuse And Implementation

Load [reuse-rules.md](references/reuse-rules.md). Map design values and components to the active project before creating or extending anything. If images or icons are involved, load [assets.md](references/assets.md).

Load [screen-architecture.md](references/screen-architecture.md) and implement only the approved contract. Follow the project's actual architecture and state-management pattern. Never invent business behavior, data, navigation, UI, or cleanup from visual implication alone.

## Phase 4 — Verification And Handoff

Load [verification.md](references/verification.md), which loads [testing.md](references/testing.md). Run focused checks and the visual convergence loop. For existing UI, compare the baseline, updated implementation, and Figma target at equivalent states and viewports.

Report contract completion, reused items, changed files, validation evidence, visual differences, blocked items, and any intentional project-over-Figma decisions.

## Always-On Guardrails

- Preserve DRY and existing consumers; do not create parallel tokens, widgets, dialogs, or business flows.
- Every implemented UI element must map to Figma, an established project convention, a platform requirement, or an approved contract item.
- Removing UI usage never implicitly authorizes deleting shared source, assets, routes, state, APIs, use cases, or analytics.
- Do not redesign or refactor unrelated UI, and never edit for an analysis-only request.
- Use Claude Code's installed Figma design-to-code skill and Figma MCP before requesting design context.
