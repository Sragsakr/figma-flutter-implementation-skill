# Discovery And Baseline

## Baseline

1. Inspect the current checkout, branch, and working-tree status.
2. Use that checkout by default. Do not create a branch or worktree unless the user explicitly asks.
3. If the user identifies a branch, verify it before editing. If the intended source is unavailable, stop before proposing replacements.

## Figma Evidence

Use the mandatory Figma design-to-code workflow before requesting design context. Inspect the target frame hierarchy, auto-layout, variants, styles, variables, assets, responsive states, annotations, and Code Connect hints.

Treat returned React/Tailwind code as a reference only. Adapt it to the target Flutter project; never paste it as implementation.

## Project Evidence

Search definitions and real usages for:

- Theme extensions, colors, typography, spacing, radii, shadows, assets, and localization.
- Existing reusable widgets and visually/functionally similar screens.
- Feature structure, main shell, routing, state management, and business-flow Cubits/use cases.

Do not conclude that a system is absent because one directory is empty or a guessed filename is missing. Identify the active definition and at least one real consumer where relevant.

## Required Inventory

Before editing, report:

1. Verified checkout and branch.
2. Existing tokens and styles that map to the Figma target.
3. Existing components/assets/screens to reuse.
4. Existing shell, routing, and state-management pattern.
5. Every confirmed gap, marked as blocked pending explicit approval.

### Widget Reuse Inventory

Before implementation, map every distinct Figma component to `reuse`, `extend`, or `blocked gap`. For each, record the closest existing widget or pattern and at least one real consumer. Include headers, navigation, input fields, tabs, cards, dialogs, states, icons, and repeated rows.

Do not create a widget until its inventory entry is complete. A different parent screen, text, spacing, or position does not change a `reuse` decision. A `blocked gap` needs the user's explicit authorization before code or assets are added.

Only proceed when the implementation can use existing items or the user has explicitly approved each gap.
