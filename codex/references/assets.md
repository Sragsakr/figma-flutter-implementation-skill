# Asset Policy

## Asset Discovery Gate

Before exporting or downloading anything from Figma:

1. Search the project's asset folders, generated asset accessors, `pubspec.yaml`, and real asset usages.
2. Reuse an existing asset only when it is visually and semantically the correct match.
3. Do not replace an existing logo, icon, illustration, or image merely because Figma supplied another copy.
4. Report a missing required asset and wait for the user's explicit approval before adding it. An asset is an addition even when it originated in Figma.

## Export Choice After Approval

Use the original Figma export; never redraw an SVG, hand-author paths, or substitute a placeholder.

| Asset type | Preferred format | Reason |
| --- | --- | --- |
| Simple icon, logo, line art, or scalable illustration | SVG | Keeps vector fidelity at all target sizes. |
| Photograph, textured image, raster illustration, or effect-heavy background | PNG | Preserves the authored pixels and effects. |
| Animated content | Existing project format only | Do not introduce a new animation package or format without approval. |

Before selecting SVG, verify the project already renders SVG with its existing tooling. Do not add an SVG dependency merely to use an SVG. If existing tooling cannot render it, report the choice and wait for approval; do not silently convert a vector into a new app convention.

## Naming And Location

Use the project's existing asset folder and naming convention. If the project has no convention and the user approves the addition, use lower_snake_case semantic names:

- `assets/icons/order_group.svg`
- `assets/images/orders_empty_state.png`
- `assets/images/orders_header_background.png`

Never use Figma node IDs, hashes, export filenames, screen names alone, `final`, `new`, or duplicate semantic names. Name by purpose, not appearance.

Keep icons, images, and illustrations in their existing separate asset directories. Register the asset through the project's existing asset manifest or asset-management file only after approval. If the application exposes an `Assets`, `AppAssets`, or generated accessor, add/regenerate the asset through that established mechanism and consume the accessor in UI code.

Never write a raw asset path such as `assets/icons/order_group.svg` inside a screen or widget. Never hand-edit generated asset code. Use the project's existing accessor or wrapper so asset locations remain centralized and can change safely.

## Asset Verification

After an approved addition, verify:

1. The file type matches the source and project support.
2. The asset is registered exactly once.
3. The generated accessor or existing app-asset wrapper resolves and is the only UI access path.
4. The UI constrains its rendered size and does not use intrinsic dimensions unexpectedly.
5. The final report identifies the source Figma item, semantic name, format, location, and consumer.
