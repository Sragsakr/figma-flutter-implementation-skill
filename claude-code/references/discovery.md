# Discovery And Baseline

## Intent Intake

Before inspecting Figma or the project, collect intent from the user in sequential steps, one question per step, waiting for each answer before the next:

1. Operation: `CREATE | SYNC | REFINE | ANALYZE`.
2. Scope: complete flow, complete screen, component, or variant/state.
3. Target: the screen, flow, component, or widget name.
4. Current implementation: route, screen class, or path, for `SYNC` and `REFINE`.
5. Exclusions or constraints, if any.

Never bundle the steps into one prompt. Skip a step only when the invocation already declares that field. Accept `unknown` or `skip`, then derive that single field from project and Figma evidence and report the derived value with its evidence in the contract.

The answers are the authoritative intent. Project instruction files (`AGENTS.md`, `CLAUDE.md`, `.cursor/rules`, `docs/`, README) and Figma evidence inform and verify the intake; they never replace the user's answers. Do not ask again for a field answered in this run.

## Baseline And Operation Mode

1. Inspect the current checkout, branch, and working-tree status.
2. Use that checkout by default. Do not create a branch or worktree unless explicitly requested.
3. If the user identifies a branch, verify it before editing.
4. Record the intake answers and their source for the operation, scope, target screen/widget, and current implementation path or symbol. Treat them as authoritative intent, not as permission to skip verification.
5. Identify the exact requested Figma scope: complete flow, complete screen, component, variant, or visual state.
6. Search the project before confirming the operation:
   - `CREATE`: no matching implementation exists after evidence-based search.
   - `SYNC`: an implementation exists and the Figma target has changed.
   - `REFINE`: the request is a bounded visual or component adjustment.
   - `ANALYZE`: the user requested no implementation.

Do not choose `CREATE` from a missing expected filename. Search routes, symbols, visible strings, feature entry points, similar components, and real consumers.

If the user-declared mode matches the evidence, adopt it. If it conflicts, do not silently override it or execute it blindly. Report:

```text
Declared operation: <mode>
Evidence-based operation: <mode>
Conflict evidence: <routes, symbols, Figma scope, or missing implementation>
Recommended next step: <confirmation needed>
```

For example, an existing route/page conflicts with declared `CREATE`, while no matching implementation after complete search conflicts with declared `SYNC`. Ask one concise confirmation before producing the contract or editing. Also stop for clarification when the checkout, target, or scope completeness cannot be verified.

## Figma Evidence

Use Claude Code's installed Figma design-to-code skill and Figma MCP before requesting design context. Inspect the target hierarchy, auto-layout, constraints, variants, variables, styles, assets, responsive states, annotations, prototype relationships, and Code Connect hints.

Classify each inspected item as a flow, screen, component, variant, or state. Record whether the supplied target is complete enough to support absence/removal decisions. A selected component, cropped screenshot, inaccessible node, or single variant is not evidence for deleting the rest of a screen.

Treat returned generated reference code as reference only. Adapt the evidence to Flutter and the active project; never paste generated reference code as implementation.

## Project Evidence

Search definitions and real usages for:

- Theme extensions, semantic colors, typography, spacing, radii, shadows, assets, localization, responsive helpers, and accessibility conventions.
- Existing reusable widgets and visually or functionally similar screens.
- Feature structure, shell, routing, state management, models, business Cubits/controllers/use cases, and navigation entry points.
- Tests, previews, golden tooling, runtime launch commands, and nearest comparable feature coverage.

Identify an active definition and at least one real consumer where relevant. Do not conclude that a system or component is absent from a sparse directory or guessed filename.

For `SYNC` and `REFINE`, also locate the current page, local sections, shared sources, registrations, assets, state, tests, and all consumers of anything that may change or be removed. Capture a rendered baseline at the target state and viewport when tooling permits; report honestly when it does not.

## Required Inventory

Before the contract, report:

1. Verified checkout, branch, mode, and scope completeness.
2. Existing tokens and styles mapped to the target.
3. Existing components, assets, screens, and patterns to reuse or extend.
4. Existing shell, routing, localization, state-management, data, and business-flow patterns.
5. Current implementation baseline for `SYNC`/`REFINE`.
6. Every confirmed gap and every material ambiguity.

### Component Reuse Inventory

Map each meaningful Figma component or section to `REUSE`, `EXTEND`, `ADD`, `BLOCKED`, or `UNCERTAIN`. Record the closest project candidate and a real consumer. Cover headers, navigation, inputs, tabs, cards, dialogs, states, icons, repeated rows, and major sections.

A different parent, label, spacing, callback, or placement is not enough reason to duplicate a component. Do not create or replace a widget until the inventory explains why reuse or extension is insufficient.

Discovery authorizes no edits. Proceed only to the Implementation Contract Gate.
