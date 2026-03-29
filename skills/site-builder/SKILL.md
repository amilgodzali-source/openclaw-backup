---
name: site-builder
description: Build and implement website features for web, mobile web, and admin panels from task lists and design references. Use when the user asks to develop UI screens, integrate APIs, refactor code, or deliver production-ready frontend/backend increments.
---

# Site Builder

## Workflow
1. Read `TASKS.md` and pick the highest-priority open task.
2. Confirm acceptance criteria from task text and design references.
3. Implement in small increments (one feature block at a time).
4. Run local checks:
   - `npm run lint` (if configured)
   - `npm run build`
   - targeted tests (if configured)
5. Update `STATUS.md` with:
   - what changed
   - files touched
   - verification results
   - known risks/blockers
6. Mark task status in `TASKS.md` (`todo` → `in_progress` → `done`).

## Implementation Rules
- Preserve existing architecture and naming conventions.
- Prefer reusable components over one-off duplication.
- Keep UI close to provided references (spacing, hierarchy, typography, CTA placement).
- Do not ship unfinished placeholders as "done".
- If requirements conflict, pause and document a decision request in `DECISIONS.md`.

## Output Format (after each block)
- ✅ Done: <short summary>
- 🧩 Files: <paths>
- 🧪 Checks: <results>
- ⚠️ Blockers: <if any>
- ⏭️ Next: <next block>
