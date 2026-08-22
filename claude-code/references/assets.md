# Asset Policy

## Discovery Gate

Before exporting, adding, replacing, or removing an asset:

1. Search asset directories, generated accessors, manifests, and real usages.
2. Reuse an asset only when it is the correct visual and semantic match.
3. Do not replace an established logo, icon, illustration, or image merely because Figma contains another copy.
4. List every new or replacement asset in the Implementation Contract with its Figma source and consumers.

## Export Choice After Approval

Use the original Figma export; never redraw vectors, author SVG paths, or substitute a placeholder.

| Asset type | Preferred format | Condition |
| --- | --- | --- |
| Simple icon, logo, line art, scalable illustration | SVG | Existing project tooling renders SVG |
| Photograph, texture, raster illustration, effect-heavy background | PNG | Preserve authored pixels/effects |
| Animated content | Existing format | New format/package requires contract approval |

Do not add an SVG or animation dependency silently. If current tooling cannot render the authored format, report the tradeoff as a gap or Plan Delta.

## Naming, Registration, And Access

Follow the existing folder and naming convention. If an approved project has none, use lower_snake_case semantic names by purpose, never Figma IDs, hashes, `final`, `new`, or screen-only vague names.

Register each asset exactly once through the established manifest or asset-management mechanism. Regenerate an existing accessor through its normal command; never hand-edit generated code. UI must use the central accessor/wrapper, never a raw asset path.

Constrain rendered dimensions explicitly when required by layout; do not rely unexpectedly on intrinsic export dimensions.

## Replacement And Removal

Distinguish:

1. Replace or remove an asset usage.
2. Remove a manifest/accessor registration.
3. Delete the source file.

Before registration removal or file deletion, search all code, tests, generated accessors, manifests, and platform consumers. An asset no longer used by the target screen may still be shared. Report a newly unused asset as an orphan candidate; delete it only when the approved contract explicitly includes registration and file deletion.

## Verification

Report the Figma source, semantic name, format, location, registration, accessor, and consumers for every added, replaced, or deleted asset. Verify type support, one registration, successful accessor resolution, and intended rendered size.
