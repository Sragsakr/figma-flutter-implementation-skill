# Asset Policy

## Discovery Gate

Search project asset folders, generated accessors, asset manifests, and real usages before exporting or downloading anything. Reuse an existing asset only when it is the correct visual and semantic match. Treat every new Figma asset as an addition that needs explicit user approval.

## Export Choice After Approval

Use the original Figma export; never redraw vectors, author SVG paths, or substitute placeholders.

- Use SVG for simple icons, logos, line art, and scalable illustrations when the project already renders SVG.
- Use PNG for photographs, textured images, raster illustrations, and effect-heavy backgrounds.
- Use only an existing project animation format for animation; request approval before adding a format or package.

## Naming, Registration, And Access

Follow the existing convention. If an approved project has none, use lower_snake_case semantic names such as `order_group.svg` or `orders_empty_state.png`; never use Figma node IDs, hashes, or vague names.

Put files in existing icon/image/illustration directories. Register them once through the existing manifest or asset-management file. Regenerate the existing `Assets` or `AppAssets` accessor when applicable; never hand-edit generated code.

Never write a raw asset path inside a screen or widget. Use the central accessor or app-asset wrapper as the single source of truth.

## Verification

Verify type support, one registration, resolved accessor, constrained render dimensions, and report the source, semantic name, format, location, and consumer.
