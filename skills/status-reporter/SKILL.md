---
name: status-reporter
description: Produce compact progress updates for ongoing development and operations. Use when the user asks for periodic reports (e.g., every 15 minutes), summaries of completed work, blockers, and next actions.
---

# Status Reporter

## Cadence
- Default: report every 15 minutes during active work.
- Immediate report on: block, incident, or milestone completion.

## Inputs
- `TASKS.md` (queue and progress)
- `STATUS.md` (latest technical updates)
- latest QA/monitoring outputs

## Message Format
- ✅ Сделано: <1-3 bullets>
- 🔄 В работе: <current block>
- ⚠️ Проблемы: <none or short list>
- ⏭️ Далее: <next concrete step>
- 🕒 ETA: <time estimate>

## Rules
- Keep reports short and factual.
- Never claim completion without check evidence.
- If blocked, state exact blocker and required input.
