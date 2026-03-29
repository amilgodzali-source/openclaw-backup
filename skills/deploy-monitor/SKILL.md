---
name: deploy-monitor
description: Monitor deployed website health, uptime, and runtime errors. Use when the user needs continuous tracking of production/staging status, incident detection, or short operational reports.
---

# Deploy Monitor

## Monitoring Scope
- Availability: app URL responds with expected HTTP status.
- Core routes: homepage, catalog, product page, cart, checkout, admin login.
- Performance baseline: response time trend.
- Runtime quality: frontend console errors and backend log errors.

## Routine
1. Check each tracked URL/route.
2. Record status code and latency.
3. Scan latest app logs for `error`, `exception`, `timeout`, `5xx`.
4. Classify incidents:
   - `P1` full outage
   - `P2` major function down
   - `P3` degraded performance/non-critical issues
5. Update `STATUS.md` monitoring section.
6. If incident exists, write action item in `TASKS.md` with priority.

## Alert Message Template
- 🚨 Incident: <P1/P2/P3>
- 🌐 Endpoint: <url/route>
- 🧾 Symptom: <what failed>
- 🕒 First seen: <timestamp>
- 🔧 Next action: <immediate mitigation>
