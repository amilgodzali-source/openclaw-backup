---
name: ui-qa-check
description: Validate UI quality and design fidelity for web/mobile/admin interfaces. Use when the user asks to compare screens against mockups, detect visual regressions, verify responsive behavior, or prepare a release candidate.
---

# UI QA Check

## QA Checklist
1. Compare target screen against reference/mockup:
   - layout structure
   - spacing and alignment
   - typography scale/weight
   - colors and component states
2. Validate responsiveness at key breakpoints:
   - mobile
   - tablet
   - desktop
3. Validate interaction states:
   - hover/focus/active/disabled
   - loading/empty/error states
4. Validate content constraints:
   - long titles
   - long prices/numbers
   - missing image fallback
5. Run technical checks:
   - console errors
   - build/lint status

## Severity
- `Critical`: blocks release, broken flows/major mismatch
- `Major`: visible quality issue, should be fixed before release
- `Minor`: polish issue, can be scheduled

## Report Format
For each issue provide:
- ID
- Severity
- Screen/Route
- Expected vs Actual
- Suggested fix
- Status (`open`, `fixed`, `retest`)
