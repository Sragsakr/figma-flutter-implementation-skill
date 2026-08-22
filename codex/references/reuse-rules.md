# Reuse Rules

## Design System

For every design value, search the active project system first.

1. Reuse an appropriate existing semantic token exactly.
2. Never use direct color literals in screens or widgets.
3. Never duplicate an equivalent token or alter an existing token's meaning for one screen.
4. Apply the same lookup-first discipline to typography, spacing, radii, shadows, icons, responsive helpers, and assets.
5. If no suitable item exists, list the precise gap and proposed addition in the Implementation Contract.

### Theme-Only Color Boundary

Every UI color must be read through the project's active theme API: `Theme.of(context).colorScheme`, a verified `ThemeExtension`, or the established theme accessor. Do not read a static palette directly from feature UI.

Do not introduce `Color(...)`, `Colors.*`, hexadecimal literals, or ad hoc local alpha transformations in UI code. Use an existing semantic state-layer/opacity helper when the project has one. Otherwise list the missing semantic value in the contract rather than working around it locally.

Choose semantic roles rather than visual values. Verify affected UI in every active theme relevant to the scope. A color correct only in one supported mode is incomplete.

## Components

Before introducing a widget, search for the same responsibility, structure, and visual role.

- Reuse an exact match.
- Extend an existing API when only content, state, actions, or slots differ and existing consumers can remain stable.
- Use composition or a base contract only for genuinely shared structure and responsibility.
- Create a screen-local widget only when the approved screen requires it and an existing API cannot represent it.
- Move an item into shared scope only when current cross-screen reuse justifies it and the contract approves the move.

Favor an existing configurable shell for dialogs, app bars, navigation, errors, loading, and empty states. Never create a screen-specific parallel merely because Figma places an established component in a new context.

### Reuse Proof

For each `ADD`, identify the closest candidate and its concrete limitation. For each `EXTEND`, identify current consumers and preserve their behavior unless the contract explicitly changes them. A plausible future reuse is not enough reason for a new abstraction.

## No Unmapped UI

Every final UI element must map to one of:

- A scoped Figma item.
- An established project shell, design-system, accessibility, or responsive convention.
- A platform requirement such as safe-area handling.
- An explicitly approved contract item.

Do not invent useful-looking icons, dividers, cards, actions, labels, empty states, gradients, shadows, or animations. Record project-preserved elements that intentionally differ from the literal frame.

## Approved Additions And Plan Deltas

The user's approval of the complete Implementation Contract authorizes its listed tokens, files, routes, local/shared components, dependencies, assets, and abstractions. Do not request repeated approval for those exact actions.

Never add or remove an unlisted capability. If implementation proves an additional change necessary, publish a focused Plan Delta with evidence, affected consumers, files, and risk. Continue only after that delta is approved.
