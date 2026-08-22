# Screen Architecture

Implement each screen as a composition root. Split it into meaningful visual sections, keep the page focused on composition and integration, and follow the project's actual folders and naming. Do not impose a new architecture.

## Component Responsibility

For every new widget in the contract, identify:

- Its screen-local or shared scope.
- Its single visual/presentation responsibility.
- The existing candidate it cannot reuse.
- State and callbacks it may receive.
- Business, navigation, or data-loading responsibilities it must not own.

Do not extract every row or spacer into a file. Extract a meaningful section, independently stateful presentation unit, or clearly reusable project concept. Keep screen-only sections local; promote them only when real current reuse and the approved contract justify it.

## State Ownership

Follow the nearest established project pattern for presentation state. Use a UI Cubit only when the project uses that pattern; use Riverpod, Bloc, Provider, ChangeNotifier, widget-local state, or another verified convention when that is the active precedent.

Keep selection, tabs, expansion, dialog visibility, and presentation validation at the smallest appropriate presentation owner. Keep business rules, persistence, API calls, and cross-feature state in existing business flows. Do not create a new state owner when existing state or simple local state is sufficient.

## Behavior And Data Boundary

Figma visual affordance alone does not authorize a tap action, route, API call, model field, analytics event, or side effect. Connect behavior only when supported by Figma annotations, an existing project flow, or the approved contract.

Treat Figma sample text and values as visual examples. Use verified models, state, and localization; never hardcode sample production data or invent a backend source. Preserve established null, empty, loading, and error behavior where the connected flow already provides it.

Do not change existing consumers as a side effect unless their change is listed in the contract.
