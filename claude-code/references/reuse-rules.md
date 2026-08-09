# Reuse Rules

## Design System

For every design value, search the active project system first.

1. Reuse an appropriate existing semantic token exactly.
2. Never use direct color literals in screens or widgets.
3. Never duplicate an equivalent token or alter an existing token's value or semantic meaning for one screen.
4. Apply lookup-first discipline to typography, spacing, radii, shadows, icons, and assets.
5. If no suitable item exists, describe the gap and wait for explicit user approval. Do not create a replacement automatically.

## Widgets

Before introducing a widget, search for one with the same responsibility and structure. Reuse an exact match; extend existing APIs for content/state/action differences; use composition or a base contract only for genuinely shared structure. Create a new widget only when directly required by the authorized screen and impossible to represent with existing APIs.

Keep screen-only widgets in the screen's local `widgets/` folder. Move anything cross-screen only with explicit authorization. Never change existing widget behavior as a side effect of one screen.

### Reuse Proof Gate

Before creating any widget, search the active project for the same responsibility, structure, and visual role. Identify the closest existing candidate and its real consumers. A different label, padding, placement, callback, or parent screen is not enough reason to duplicate it.

This applies to every widget type, including top bars, app bars, headers, status indicators, navigation, inputs, tabs, cards, buttons, dialogs, lists, empty states, loading states, and feature controls. Reuse the existing widget and its established state source whenever it serves the same responsibility; never create a screen-specific parallel version merely because Figma places it on another screen.

Create a replacement only when the existing candidate cannot meet the required responsibility through its current API. Before doing so, report the candidate, its concrete limitation, and the user's explicit authorization.

## Unapproved Additions

Never add a token, color, type style, spacing/shadow/radius definition, theme file, route, feature boundary, shared widget, shell component, dependency, asset, or abstraction unless the user explicitly requested that exact addition. Report the missing capability and stop for approval.
