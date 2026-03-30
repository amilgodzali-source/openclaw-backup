# MASTER_DASHBOARD.md

Обновлено: 2026-03-29 UTC

## 1) Главное сейчас
- Проект: маркетплейс одежды/обуви (web + mobile + админка)
- Цель: построить «офис» ИИ-агентов для автоматизации операционки
- OpenClaw: обновлён до `2026.3.28`
- Канал: Telegram подключен и работает

---

## 2) Проекты и файлы

### Основные артефакты
- `homepage-v1.html`
- `WORDPRESS_BOT_PLAYBOOK.md`
- `myshop-project-current-2026-03-11.zip`
- `myshop-project-ready.zip`

### Управление задачами
- `STATUS.md` — общий статус
- `TASKS.md` — очередь задач (P0/P1)
- `DECISIONS.md` — принятые решения
- `SESSIONS_LOG.md` — журнал сессий

---

## 3) Установленные скиллы
- `skills/agent-browser`
- `skills/deploy-monitor`
- `skills/find-skills`
- `skills/github`
- `skills/self-improving-agent`
- `skills/site-builder`
- `skills/status-reporter`
- `skills/task-orchestrator`
- `skills/ui-qa-check`

---

## 4) Автоматизации (cron)
- `08:00` — healthcheck
- `14:00` — healthcheck
- `22:30` — nightly backup

Скрипты:
- `scripts/openclaw_healthcheck.sh`
- `scripts/nightly_backup.sh`

Логи:
- `logs/cron_health.log`
- `logs/cron_backup.log`

---

## 5) Backup / GitHub
- Репозиторий: `https://github.com/amilgodzali-source/openclaw-backup`
- Ветка: `main`
- Автокоммит и push: nightly (22:30)

---

## 6) Безопасность
Сделано:
- `channels.telegram.groupPolicy` -> `allowlist`
- отключён `gateway.controlUi.dangerouslyDisableDeviceAuth`
- добавлен `gateway.auth.rateLimit`
- ужесточены права на чувствительные файлы/папки

Текущий итог:
- Security audit: `0 critical · 1 warn · 1 info`

Оставшийся warning:
- `gateway.nodes.denyCommands` содержит неэффективные command IDs (можно дочистить отдельно)

---

## 7) Память и контекст
- Long-term: `MEMORY.md`
- User profile: `USER.md`
- Daily notes: `memory/YYYY-MM-DD.md`
- Техсводка: `OFFICE_SETUP_STATUS.md`

---

## 8) Быстрая проверка (если что-то сломалось)
1. `openclaw status --deep`
2. `openclaw logs --follow`
3. `openclaw security audit --deep`
4. `crontab -l`

---

## 9) Следующие шаги (практично)
1. Дочистить warning по `denyCommands`
2. Запустить 3 боевых агента (Sales, Support, WordPress)
3. Включить ежедневный отчёт владельцу в Telegram (утро/вечер)
4. Перевести в этап 2: Catalog + Analytics + Logistics
