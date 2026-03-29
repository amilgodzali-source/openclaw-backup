---
name: task-orchestrator
description: Coordinate task execution across build, QA, and monitoring flows. Use when the user needs prioritization, dependency management, execution order, or clear next-step planning for website delivery.
---

# Task Orchestrator

## Source of Truth Files
- `TASKS.md` — all tasks and statuses
- `STATUS.md` — current execution state
- `DECISIONS.md` — accepted trade-offs and approvals

## Orchestration Steps
1. Normalize tasks to a common schema:
   - `id`, `title`, `priority`, `owner`, `status`, `depends_on`, `eta`
2. Build execution queue:
   - unblock critical path first
   - prioritize `P0/P1`
   - avoid parallel work on dependent tasks
3. Dispatch flow:
   - Build task → QA check → done
   - If QA fails: reopen with exact fix scope
4. Keep WIP low:
   - max 1-2 active engineering tasks at once
5. Replan on blockers and update queue immediately.

## Status Values
- `todo`
- `in_progress`
- `qa`
- `blocked`
- `done`

## Daily Summary Format
- Completed today
- In progress
- Blocked (with reason)
- Next 3 tasks by priority
