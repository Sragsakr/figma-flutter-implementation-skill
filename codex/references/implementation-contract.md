# Implementation Contract

The contract turns discovery into a reviewable execution boundary. Publish it before any edit. Keep it proportional to the scope and concise enough to review, but make every material addition, modification, removal, and blocked decision explicit. Mark a non-applicable section `N/A` rather than manufacturing content for it.

## Required Header

```text
Operation: CREATE | SYNC | REFINE | ANALYZE
Target: <screen, component, or flow>
Figma scope: <full flow, full screen, component, or state>
Current implementation: found | not found | uncertain
In scope: <items>
Out of scope: <items>
```

Do not classify a request as `CREATE` merely because an expected filename is absent. Search routes, symbols, visible text, components, and real consumers first.

## Action Vocabulary

Assign one action to every material item:

- `ADD`: introduce an approved item.
- `MODIFY`: change an existing item in place.
- `REMOVE`: remove the specifically named item at the stated layer.
- `REMOVE USAGE`: stop consuming an item without deleting its source.
- `REUSE`: use an existing item unchanged.
- `EXTEND`: expand an existing API while preserving current consumers.
- `REPLACE`: replace a named implementation or composition.
- `MOVE`: relocate without changing responsibility.
- `KEEP` or `UNCHANGED`: reviewed and intentionally retained.
- `BLOCKED`: a confirmed gap requires approval or missing input.
- `UNCERTAIN`: evidence is insufficient; do not implement or remove it.

Avoid vague actions such as “match Figma,” “update as needed,” or “clean old code.”

## Required Tree

For `CREATE`, show what will be built. For `SYNC` or `REFINE`, show the current-to-target actions.

```text
Target Flow [CREATE or SYNC]
├── Navigation
│   └── Existing route [REUSE]
├── TargetPage [ADD or MODIFY]
│   ├── ExistingHeader [REUSE]
│   ├── SummarySection [ADD or MODIFY]
│   └── LegacyBanner [REMOVE USAGE]
├── State
│   ├── Existing business state [KEEP]
│   └── Local selection [ADD: PRESENTATION]
├── Assets
│   └── target_icon.svg [ADD]
└── Verification
    ├── Focused test [ADD or MODIFY]
    └── Visual comparison [REQUIRED]
```

The tree must distinguish removing a consumer from deleting its source.

## Required Action Table

| ID | Target | Action | Figma evidence | Project evidence | Decision | Expected files | Risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UI-01 | Header | REUSE | Node or annotation | Symbol and consumer | Use unchanged | None | Low |

Use stable IDs such as `UI-`, `ST-`, `NAV-`, `AS-`, `DS-`, `BL-`, and `TEST-`. Cite a Figma node/variant when available and a code symbol/path plus real consumer when relevant.

## Required Supporting Sections

1. **Evidence ledger:** facts from Figma and code, separated from implementation decisions.
2. **Expected changed files:** each file and why it is in scope. Mark files whose exact path depends on project convention.
3. **New additions:** tokens, files, routes, assets, dependencies, shared APIs, and abstractions.
4. **Destructive changes:** separate UI removal, usage removal, registration removal, source deletion, state deletion, and business deletion.
5. **Blocked and uncertain items:** missing evidence and the smallest clarification needed.
6. **Verification plan:** target states, viewports, focused analysis/tests, and visual evidence.

For `CREATE`, also include the coverage, behavior, data, state, and architecture sections required by [create-workflow.md](create-workflow.md). For `SYNC` and `REFINE`, include the baseline and deletion evidence required by [change-reconciliation.md](change-reconciliation.md).

## Approval And Plan Delta

Ask for one decision after the complete contract:

1. Approve all listed actions.
2. Approve with named exclusions.
3. Revise the contract.

Approval authorizes only listed actions. Do not repeatedly ask about approved files or additions.

If an unexpected requirement appears, pause only the affected work and publish:

```text
Plan Delta: <number>
Unexpected evidence: <fact>
Original decision: <action and ID>
Proposed change: <precise action>
Affected files and consumers: <list>
Scope and risk impact: <summary>
```

Continue unaffected approved work only when doing so cannot prejudice the pending decision.
