# Create Workflow

Preserve the skill's reuse-first creation behavior. These gates reduce omission, visual invention, speculative behavior, and over-architecture without turning every implementation detail into a separate approval.

## Create Readiness

Before writing the contract, verify:

- Target frames and their boundaries.
- Whether each node is a screen, component, variant, or responsive state.
- Auto-layout, constraints, scrolling, overlays, and annotations.
- Required assets and whether they are accessible.
- Navigation relationships shown or documented.
- The project entry point, shell, and nearest comparable screen.
- Ambiguities that affect structure, data, behavior, or navigation.

Use project precedent for a minor implementation detail only when it does not alter product behavior or the visual intent. Mark consequential ambiguity `BLOCKED` or `UNCERTAIN`; never fill it with a plausible invention.

## Figma Coverage Matrix

Map each meaningful scoped screen, section, component, asset, and state. Do not enumerate decorative leaf nodes that add no review value.

| Figma item | Role | Flutter mapping | Action | Evidence or gap |
| --- | --- | --- | --- | --- |
| Node/variant | Header | Existing header | REUSE | Symbol plus consumer |

Every meaningful target item must be mapped, blocked, or explicitly excluded. Conversely, every final UI element must come from Figma, an established project shell/design-system convention, a platform requirement, or an approved contract item.

Do not add plausible but unmapped dividers, icons, cards, actions, empty states, gradients, labels, animations, or decorations.

## Behavior And Data Evidence

For each meaningful interaction, state what authorizes its behavior:

| Control | Figma evidence | Existing project behavior | Decision |
| --- | --- | --- | --- |

A visual affordance does not prove navigation or a business action. A card is not tappable merely because tapping would be useful. Reuse documented annotations or existing flows; otherwise keep it non-interactive or block it.

For each dynamic field, identify its real source:

| UI field | Existing model/state source | Null/empty handling | Decision |
| --- | --- | --- | --- |

Figma sample text is display evidence, not proof of a production value, model field, API, or localization key. Never hardcode sample data in production or invent a backend source.

## State Coverage

List all states supported by Figma or the existing flow: initial, loading, content, empty, error, disabled, selected, expanded, and responsive variants as applicable. Implement only evidenced states. Preserve an established project-level state when the connected flow already emits it, even when Figma shows only the content state; use the project's existing presentation pattern rather than inventing a new design.

## Architecture Budget

Make architecture growth visible in the contract:

```text
New screens: <count>
New screen-local widgets: <count>
Extended shared widgets: <count>
New presentation-state owners: <count>
New business state/use cases/repositories: <count>
New routes/assets/dependencies/tokens: <count>
```

Prefer zero new business layers and dependencies for a visual implementation. A budget is a review boundary, not a target. Exceeding an approved category requires a Plan Delta.

## Implementation Passes

1. **Structure:** shell, hierarchy, constraints, scroll behavior, safe areas, and responsive composition.
2. **Design system:** verified typography, semantic colors, spacing, radii, shadows, and assets.
3. **State and behavior:** connect only approved existing or presentation behavior.
4. **Content stress:** exercise relevant long, empty, nullable, loading, keyboard, text-scale, and RTL conditions supported by the project.
5. **Convergence and cleanup:** compare visually, fix scoped differences, remove accidental duplication, then validate.

These are reasoning checkpoints, not a requirement to leave incomplete commits or ask for approval between passes.
