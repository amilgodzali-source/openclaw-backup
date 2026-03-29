# HEARTBEAT.md

## Periodic Tasks

### Save Session Summary (every 30 minutes)
Read the current conversation context and append a summary to `SESSIONS_LOG.md` in the workspace.

Format:
```
## [DATE TIME]
**Topics discussed:** ...
**Decisions made:** ...
**Plans & todos:** ...
**New info about user:** ...
---
```

Also update `USER.md` if any new personal info was shared.
