# Testing Policy

## Discovery Gate

Inspect existing test dependencies, test folders, helpers, mocks, naming, and the closest comparable test. Reuse them. Never add a test dependency, harness, mock library, or golden framework without explicit approval.

## Required Coverage

- For a UI Cubit, test initial state and every new transition.
- For a screen interaction, add a widget test only when the project already supports it.
- For an existing business integration, reuse its tests; do not invent behavior from Figma.
- For pure visuals, use existing golden/visual tooling or report manual comparison at target Figma size.

Do not write tests only to increase coverage. Report missing test infrastructure as a gap.

## Validation Sequence

Format changed Dart files, run focused analysis, run focused tests, run relevant established broader checks, run `git diff --check`, and inspect final changed files against scope. Keep unrelated existing failures separate.
