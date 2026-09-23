# День 0 — чек-лист проекта `<project>`

День 0 считается пройденным, когда **сквозная функция работает в проде**: один реальный
вход проходит через все узлы системы до видимого владельцу результата, и каждый узел на
этом пути закрыт гейтом (R0.3). Не «каркас написан», а «каркас ходит».

Пока в этом файле есть хоть один незакрытый пункт, `scripts/day0_check.py` завершается
кодом 1 и гейт CI красный. Это сделано намеренно: день 0 не «размазывается» по кварталу.

**Как закрыть пункт.** Пункт закрывается, когда работа сделана: `- [x]`.

**Как пропустить пункт.** Пункт можно пропустить только со ссылкой на ADR, объясняющий
почему именно этот проект живёт без него:

```
  - [ ] R6.5 — Бэкап и restore-тест — ... [skip: ADR-0007]
```

ADR с этим номером обязан существовать (`docs/adr/0007-*.md`) — иначе `day0_check.py`
считает пункт открытым и печатает `skip without ADR`. Пропуск без ADR невозможен:
«потом напишем» здесь не работает.

**Пункты, которые требуют кода скелета** (R2.3 кодоген контракта, R2.5 реестр флагов,
R3.4 `best_effort()`), закрываются вместе с walking skeleton — до этого они открыты, и это
нормальное состояние свежего проекта.

Каждая строка ссылается на регламент по коду; сами регламенты живут в каталоге `ai_tools`
и в проект не копируются.

## Чек-лист

### R0. Основание

- [ ] R0.1 — Конституция проекта — заполнить `CLAUDE.md`: принципы проекта, таблица прав агента, ≤ 60 строк, только ссылки — [R0.1](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R0.1-project-constitution.md)
- [ ] R0.2 — Структура репозитория и template-репо — репозиторий развёрнут из этого шаблона, `.secrets/` в `.gitignore` до появления первых кредов — [R0.2](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R0.2-repo-structure-and-template.md)
- [ ] R0.3 — Старт проекта «день 0» — пройти этот чек-лист и закрыть его сквозной функцией в проде, а не готовностью файлов — [R0.3](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R0.3-day0-walking-skeleton.md)
- [ ] R0.4 — Реестр регламентов и уроков — поставить в `CLAUDE.md` ссылку на R-каталог `ai_tools`; урок сессии становится строкой регламента в той же сессии — [R0.4](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R0.4-regulations-and-lessons-registry.md)

### R1. Постановка и поток работ

- [ ] R1.1 — Definition of Ready — записать критерий входа задачи: замер (число, популяция, дата, место), гипотеза, критерий готовности — [R1.1](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R1.1-definition-of-ready.md)
- [ ] R1.2 — Политика дефектов «класс или закрыть» — завести доску с WIP-лимитом Inbox; карточка только на класс дефектов с названным сторожем — [R1.2](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R1.2-defect-policy-class-or-close.md)

### R2. Архитектура

- [ ] R2.1 — Принципы архитектуры класса проектов — выбрать принципы проекта и для каждого назвать автопроверку, которая его стережёт — [R2.1](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R2.1-architecture-principles.md)
- [ ] R2.2 — ADR — завести `docs/adr/`, принять правило «ADR до кода», написать ADR-0001 о выбранной архитектуре и деплой-юнитах — [R2.2](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R2.2-adr.md)
- [ ] R2.3 — Контракты: единственный источник и генерация — один источник контракта, клиентские типы генерируются, `regen-diff = 0` стоит шагом гейта — [R2.3](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R2.3-contracts-single-source.md)
- [ ] R2.4 — Модель данных и миграции — статусы и периоды enum'ом в БД, один head, `lock_timeout`, NULL не значит состояние — [R2.4](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R2.4-data-model-and-migrations.md)
- [ ] R2.5 — Конфигурация и флаги — один путь чтения конфига и реестр параметров и флагов, у каждого флага владелец и `remove_by` — [R2.5](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R2.5-config-and-flags.md)

### R3. Разработка

- [ ] R3.1 — Цикл фичи — зафиксировать, что фича идёт сессией профильного скилла `ai_tools`: spec → красный тест реального пути → код → ревью → деплой → телеметрия — [R3.1](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R3.1-feature-cycle.md)
- [ ] R3.2 — Малые изменения — записать предел размера PR, правило «один класс изменений на PR» и запрет «поправь, что заметишь» без воспроизведённого отказа — [R3.2](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R3.2-small-changes.md)
- [ ] R3.3 — Стиль, линтеры, типы — настроить `ruff` и `mypy` (и `tsc`/`eslint`, если есть фронтенд) и поставить их шагами безусловного гейта — [R3.3](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R3.3-style-linters-types.md)
- [ ] R3.4 — Обработка отказов — завести `best_effort(site)` с метрикой и savepoint; `BLE001`/`S110`/`E722` делают PR красным — [R3.4](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R3.4-failure-handling.md)
- [ ] R3.5 — Гигиена веток и рабочих деревьев агентов — worktree на агента в `.claude/worktrees/`, `git status` каждого дерева перед мержем, общий чекаут не трогается — [R3.5](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R3.5-branch-and-worktree-hygiene.md)
- [ ] R3.6 — Права и действия агента — заполнить таблицу прав агента в `CLAUDE.md` под этот проект: что без спроса, что через вопрос, что никогда — [R3.6](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R3.6-agent-permissions-and-actions.md)

### R4. Качество

- [ ] R4.1 — Пирамида тестов и обязательные ярусы на PR — описать в `docs/testing.md` ярусы проекта: какие заведены, чем запускаются, чего осознанно нет — [R4.1](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R4.1-testing-pyramid.md)
- [ ] R4.2 — Гейт CI — один безусловный джоб в `.github/workflows/gate.yml`: без `paths:`, без `continue-on-error`, `--strict-markers`, allowlist пуст — [R4.2](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R4.2-ci-gate.md)
- [ ] R4.3 — Сторожа и мутации — принять правило: новый сторож доказывает себя мутацией, доказательство — в описании PR — [R4.3](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R4.3-guards-and-mutations.md)
- [ ] R4.4 — Код-ревью — ревью делает независимый ревьюер по фиксированному списку аспектов и с перемером своей выборкой, вердикт из трёх — [R4.4](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R4.4-code-review.md)
- [ ] R4.5 — Definition of Done — записать DoD: класс и сторож названы, телеметрия под SLO, документ обновлён, приёмка на проде — [R4.5](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R4.5-definition-of-done.md)

### R5. Поставка

- [ ] R5.1 — Деплой — один workflow деплоя, и записано, где живёт боевой compose или манифест — [R5.1](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R5.1-deploy.md)
- [ ] R5.2 — Миграции в проде — порядок «схема до кода», один head и `lock_timeout` проверяются гейтом, а не памятью — [R5.2](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R5.2-prod-migrations.md)

### R6. Эксплуатация

- [ ] R6.1 — SLO и алерты — завести 5–7 симптомных правил, `noDataState` не считается OK, у каждого правила есть действие — [R6.1](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R6.1-slo-and-alerts.md)
- [ ] R6.2 — Телеметрия — размечать границы и только то, что нужно для SLO; разметка каждой операции запрещена — [R6.2](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R6.2-telemetry.md)
- [ ] R6.5 — Бэкап и restore-тест — настроить бэкап и доказать его восстановлением на пустой стенд, а не наличием файлов — [R6.5](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R6.5-backup-and-restore-test.md)

### R7. Сессия и агенты

- [ ] R7.4 — Харнес агента — файл прогресса сессии в `.claude/notes/<тема>/`, требования failing-by-default, ограничения в файле, а не в контексте — [R7.4](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R7.4-agent-harness.md)
- [ ] R7.5 — Параллелизм агентов — задать WIP-лимит агентов: один модуль на агента, независимость по файлам, мерж по одному — [R7.5](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/R7.5-agent-parallelism.md)
