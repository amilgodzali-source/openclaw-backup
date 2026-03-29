# Errors Log

Command failures, exceptions, and unexpected behaviors.

---
## [ERR-20260308-001] browser-tool-no-local-browser

**Logged**: 2026-03-08T17:07:33Z
**Priority**: high
**Status**: pending
**Area**: infra

### Summary
Browser automation tool failed because no supported local browser was found.

### Error
```
Error: No supported browser found (Chrome/Brave/Edge/Chromium on macOS, Linux, or Windows).
```

### Context
- Operation attempted: browser.open https://www.google.com
- Environment: host runtime

### Suggested Fix
Install a supported browser binary (Chromium/Chrome) accessible to OpenClaw browser tool, or route browser actions through a connected node profile.

### Metadata
- Reproducible: yes
- Related Files: /root/.openclaw/workspace/skills/agent-browser/SKILL.md

---

## [ERR-20260308-002] memory-search-embeddings-auth

**Logged**: 2026-03-08T17:07:33Z
**Priority**: high
**Status**: pending
**Area**: config

### Summary
memory_search is unavailable due to embedding provider auth error.

### Error
```
openai embeddings failed: 401 invalid_api_key
```

### Context
- Operation attempted: memory_search("Амиль Годжаев закупки 1688 ...")

### Suggested Fix
Fix embeddings provider API key or switch embeddings to a working provider.

### Metadata
- Reproducible: yes
- Related Files: /root/.openclaw/workspace/MEMORY.md

---
