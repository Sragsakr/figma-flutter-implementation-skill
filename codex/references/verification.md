# Verification And Handoff

## Verification

1. Load [testing.md](testing.md) and run the required focused checks using existing project commands.
2. Check formatting and verify the diff has no accidental changes.
3. Compare the implemented screen with the Figma frame at relevant device sizes.
4. Preserve established shell, shared widgets, and system values when they differ from Figma unless the user approves their change.

Do not modify unrelated files merely to make a broad analyzer result clean. If an unrelated existing failure appears, report it separately.

## Handoff

Report:

- Verified baseline and implementation status.
- Existing tokens, components, assets, and flows reused.
- Files changed and why each is directly within scope.
- Validation commands and results.
- Remaining visual differences, missing assets, and blocked items.
- Confirmation that no unapproved additions were made.
