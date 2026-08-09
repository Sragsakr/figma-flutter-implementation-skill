# Screen Architecture

Implement each screen as a composition root. Split the UI into meaningful visual sections and keep screen-only sections in the feature's local `widgets/` folder. Follow the actual project structure; do not impose a new architecture.

Use `ScreenNameUiCubit` only for presentation state such as selection, tabs, local loading, expansion, dialog visibility, and presentation validation. Keep business rules out of this Cubit. Reuse existing business Cubits/use cases and do not invent API calls, business actions, or navigation flows.
