# Screen Architecture

Implement each screen as a composition root.

- Split the UI into meaningful visual sections.
- Keep the page focused on composition, providers, and connection to existing navigation.
- Place screen-only sections in the feature's local `widgets/` folder.
- Follow the actual project folder and naming conventions; do not impose a new architecture.

## State Ownership

Use `ScreenNameUiCubit` only for that screen's presentation state: selection, tabs, local loading, expansion, dialog visibility, and presentation validation.

Keep business rules out of the UI Cubit. Reuse the existing feature Cubits/use cases for business flows. A nested component with an independent business flow owns a separate Cubit only when that pattern already exists or the user explicitly authorizes it.

Do not invent business actions, API calls, or navigation flows not supplied by the user or already present in the project.
