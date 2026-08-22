# Verification And Handoff

Load [testing.md](testing.md) and use the project's established commands.

## Contract Audit

Before visual claims, compare the final diff to the approved contract:

- Every changed file maps to an approved action or Plan Delta.
- Every meaningful scoped Figma item is implemented, blocked, or explicitly excluded.
- No unexplained UI, business behavior, data source, dependency, token, asset, route, or abstraction was added.
- Removed usages and deleted sources match their separately approved layers.
- Shared consumers remain stable unless explicitly included.

## Visual Convergence Loop

Verify the same relevant state and viewport in Figma and Flutter.

1. Capture the target Figma reference and dimensions.
2. For `SYNC`/`REFINE`, retain the pre-edit baseline when runtime tooling permits.
3. Capture the implementation after the approved changes.
4. Compare hierarchy, visibility, ordering, geometry, spacing, typography, semantic colors, assets, borders, shadows, clipping, scrolling, safe areas, and responsive/state variants.
5. Classify each difference as `FIX`, `INTENTIONAL`, `BLOCKED`, or `OUT OF SCOPE`.
6. Fix scoped differences and repeat capture/comparison until no unexplained scoped difference remains.

Do not claim a screenshot, runtime check, theme check, or pixel match that was not performed. If capture tooling is unavailable, state the limitation and provide the strongest available static/runtime evidence.

Preserve established project shell, accessibility, responsive, and system behavior when it intentionally differs from a literal Figma frame, unless the contract approves changing it.

## Content And State Stress

Exercise only relevant states supported by Figma or the connected project flow: loading, content, empty, error, selected, disabled, expanded, long/nullable content, text scaling, keyboard, RTL, alternate themes, and supported viewports. Do not invent new product states merely for verification.

## Difference Table

Report material differences:

| Area | Target | Result | Status | Evidence or reason |
| --- | --- | --- | --- | --- |

`INTENTIONAL` requires a project convention or approved decision. `BLOCKED` requires the missing capability or evidence. Never hide a remaining mismatch behind a general “matches Figma” statement.

## Handoff

Report:

- Operation, verified baseline, and contract completion.
- Existing tokens, components, assets, state, and flows reused or extended.
- Changed files and their action IDs.
- Validation commands and results.
- Visual comparison evidence and remaining difference table.
- Blocked/uncertain items and approved exclusions.
- Confirmation that no unapproved additions or destructive changes were made.
