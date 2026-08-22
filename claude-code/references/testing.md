# Testing Policy

## Discovery

Before changing tests, inspect existing dependencies, folders, helpers, mocks, naming, and the closest comparable tests. Reuse that setup. Do not add a test dependency, harness, mock library, or golden framework unless it is listed in the approved contract.

## Risk-Based Coverage

Test behavior introduced or changed by the contract, not implementation trivia or framework internals.

| Changed behavior | Focused evidence |
| --- | --- |
| Presentation-state logic | Unit test meaningful initial state and transitions |
| User interaction | Widget test visible result when project support exists |
| Existing business-flow connection | Reuse or adjust its established tests; never invent API behavior |
| Navigation change | Existing routing/widget test pattern when available |
| Pure visual layout | Existing golden/visual tooling, otherwise recorded screenshot comparison |
| Removal | Update affected tests and prove remaining consumers still build/pass |

Simple local state does not require a new Cubit solely to make it unit-testable. Do not add tests only to increase coverage. If required infrastructure is absent, report the limitation rather than creating an unapproved framework.

## Validation Sequence

1. Format changed Dart files using project commands.
2. Run focused static analysis on changed production and test files.
3. Run focused unit/widget/golden tests relevant to the contract.
4. Run an established broader check only when relevant.
5. Run `git diff --check` and inspect the final changed-file list against the approved tree/table.
6. For shared changes or deletions, verify affected consumers.

Separate pre-existing unrelated failures from introduced failures. Never edit unrelated code merely to make a broad command pass.
