# Change Reconciliation

Use this workflow for `SYNC` and `REFINE`. Reconcile the current Flutter implementation with the current Figma target; do not rebuild a working screen merely because its design changed.

## Establish The Baseline

Before editing:

1. Locate the actual route, page, local sections, shared components, state sources, assets, and tests.
2. Identify real consumers of every shared item that may be changed or removed.
3. Capture the current rendered state at the target viewport when runtime tooling is available. If it is unavailable, record the limitation and use code evidence; do not claim a visual baseline was captured.
4. Confirm whether the supplied Figma scope is a complete flow/screen or only a component, variant, or state.

## Compare Current To Target

Classify each meaningful item as `ADD`, `MODIFY`, `REMOVE`, `REMOVE USAGE`, `REUSE`, `EXTEND`, `REPLACE`, `MOVE`, `KEEP`, `UNCHANGED`, `BLOCKED`, or `UNCERTAIN`.

Compare separately:

- Hierarchy, visibility, ordering, and responsive behavior.
- Typography, semantic colors, spacing, radii, borders, and shadows.
- Components and their APIs.
- Content, localization, and data source.
- Presentation state and business state.
- Interactions, navigation, and side effects.
- Assets and asset registrations.
- Tests and visual evidence.

Prefer a minimal in-place change that preserves established APIs and consumers. Do not create a parallel “new” screen or widget unless the approved contract explains why the current implementation cannot represent the target.

## Absence Is Not Automatically Removal

An item absent from Figma may be removed only when the evidence establishes that:

- The inspected target is the complete relevant screen/flow/state.
- The item is not present in another target variant or responsive state.
- It is not conditionally visible according to annotations or existing behavior.
- Its removal is inside the authorized scope.

Otherwise mark it `UNCERTAIN` and retain it pending clarification. Never infer removals from an inaccessible node, cropped screenshot, selected component, or partial frame.

## Deletion Layers

Make a separate decision for each affected layer:

1. Remove from layout.
2. Remove widget or asset usage.
3. Remove route or registration.
4. Delete screen-local source.
5. Delete shared source or asset file.
6. Remove presentation state.
7. Remove business state, use case, repository, API, analytics, or permission.

Authorization at one layer does not authorize another. Before source deletion, search definitions, generated accessors, registrations, tests, and every consumer. If an item becomes unused, report it as an orphan candidate; delete it only when the contract explicitly includes that deletion.

A disappearing visual control does not prove that its business capability should be deleted. Business deletion requires an explicit user requirement or non-visual product/technical evidence.

## Update Contract Requirements

In addition to the common contract, include:

- Current implementation baseline.
- Change tree grouped by navigation, UI, state, assets, and verification.
- Before-to-target action table.
- A destructive-changes table stating what is removed, what remains, consumer evidence, and risk.
- `KEEP` decisions for important logic or shared sources that might otherwise look obsolete.
- Baseline, target, and after-implementation comparison plan.

If implementation uncovers a difference not represented in the approved table, use a Plan Delta rather than silently broadening the sync.
