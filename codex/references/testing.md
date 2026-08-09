# Testing Policy

## Test Discovery Gate

Before writing a test, inspect the existing project test structure, test dependencies, mocks, helpers, naming, and the nearest comparable feature test. Reuse that pattern. Do not add a testing dependency, test harness, mock library, or golden-test framework without explicit approval.

## Required Coverage

Add only tests that directly prove newly introduced behavior and fit the existing test setup.

| Changed behavior | Required focused test |
| --- | --- |
| Screen UI Cubit state | Unit test initial state plus every transition introduced by the screen. |
| Screen interaction wired to local state | Widget test for the visible state change when the project already supports widget tests. |
| Existing business flow integration | Reuse its existing Cubit/use-case tests; do not invent API behavior from Figma. |
| Pure visual layout | Use existing golden/visual test tooling when present; otherwise report manual comparison at the target Figma size. |

Do not create tests solely to increase coverage and do not test framework internals. If a test setup is missing or incompatible, report the exact limitation and wait for approval before adding infrastructure.

## Validation Sequence

1. Format changed Dart files with the project's standard formatter.
2. Run focused static analysis on changed production and test files.
3. Run focused unit/widget tests.
4. Run the project’s required broader check only when it is already established and relevant.
5. Run `git diff --check` and inspect the final changed-file list against the approved scope.

Separate pre-existing unrelated failures from failures caused by the new screen. Never edit unrelated code merely to make a broad command pass.
