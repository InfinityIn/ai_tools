# Регламенты

Правила, общие для всех проектов владельца. Регламент отвечает на вопрос
«как это делается у нас» и живёт дольше любой фичи и любого репозитория.

**Регламент подключается в проект ссылкой из `CLAUDE.md` проекта, не копией:**
копии расходятся молча. Раскладка, специфичная для проекта (что заведено, чем
запускается, чего осознанно нет), пишется в документе самого проекта и ссылается
на регламент, а не пересказывает его.

Отличие от конвенций рядом (`../repo-structure.md`): конвенция описывает форму,
регламент — процесс и критерии.

Каталог построен 2026-09-23 по villas
`.claude/notes/bug_stream_root_causes_2026_09_22/13_target_operating_model.md` §4.

## R0. Основание

| Код | Название | Ур. | Д0/E | Статус | Файл |
|---|---|---|---|---|---|
| R0.1 | Конституция проекта (CLAUDE.md/AGENTS.md) | B | Д0 | `stub` | [R0.1-project-constitution.md](R0.1-project-constitution.md) |
| R0.2 | Структура репозитория и template-репо | A | Д0 | `draft` | [R0.2-repo-structure-and-template.md](R0.2-repo-structure-and-template.md) |
| R0.3 | Старт проекта — «день 0» (walking skeleton) | A | Д0 | `stub` | [R0.3-day0-walking-skeleton.md](R0.3-day0-walking-skeleton.md) |
| R0.4 | Реестр регламентов и уроков | A | Д0 | `draft` | [R0.4-regulations-and-lessons-registry.md](R0.4-regulations-and-lessons-registry.md) |
| R0.5 | Секреты, доступы, break-glass | A | — | `stub` | [R0.5-secrets-access-breakglass.md](R0.5-secrets-access-breakglass.md) |

## R1. Постановка и поток работ

| Код | Название | Ур. | Д0/E | Статус | Файл |
|---|---|---|---|---|---|
| R1.1 | Definition of Ready | A | Д0 | `draft` | [R1.1-definition-of-ready.md](R1.1-definition-of-ready.md) |
| R1.2 | Политика дефектов: «класс или закрыть» | A | Д0 | `draft` | [R1.2-defect-policy-class-or-close.md](R1.2-defect-policy-class-or-close.md) |
| R1.3 | Discovery vs delivery | A | — | `stub` | [R1.3-discovery-vs-delivery.md](R1.3-discovery-vs-delivery.md) |
| R1.4 | Спецификация фичи | B | — | `draft` | [R1.4-feature-spec.md](R1.4-feature-spec.md) |
| R1.5 | Решения владельца и вопросы | A | — | `active` | [R1.5-owner-decisions-and-questions.md](R1.5-owner-decisions-and-questions.md) |
| R1.6 | Доска: колонки, коды, дубли | B | — | `active` | [R1.6-board-columns-codes-duplicates.md](R1.6-board-columns-codes-duplicates.md) |
| R1.7 | Метрики потока | A | E | `stub` | [R1.7-flow-metrics.md](R1.7-flow-metrics.md) |
| R1.8 | Ритуалы | A | E | `stub` | [R1.8-rituals.md](R1.8-rituals.md) |

## R2. Архитектура

| Код | Название | Ур. | Д0/E | Статус | Файл |
|---|---|---|---|---|---|
| R2.1 | Принципы архитектуры класса проектов | A | Д0 | `stub` | [R2.1-architecture-principles.md](R2.1-architecture-principles.md) |
| R2.2 | ADR | B | Д0 | `stub` | [R2.2-adr.md](R2.2-adr.md) |
| R2.3 | Контракты: единственный источник и генерация | A | Д0 | `stub` | [R2.3-contracts-single-source.md](R2.3-contracts-single-source.md) |
| R2.4 | Модель данных и миграции | A | Д0 | `stub` | [R2.4-data-model-and-migrations.md](R2.4-data-model-and-migrations.md) |
| R2.5 | Конфигурация и флаги | A | Д0 | `stub` | [R2.5-config-and-flags.md](R2.5-config-and-flags.md) |
| R2.6 | Границы модулей и деплой-юниты | B | — | `stub` | [R2.6-module-boundaries-deploy-units.md](R2.6-module-boundaries-deploy-units.md) |
| R2.7 | LLM-слой | A | E | `stub` | [R2.7-llm-layer.md](R2.7-llm-layer.md) |
| R2.8 | Конвейер приёма данных | A | — | `stub` | [R2.8-ingestion-pipeline.md](R2.8-ingestion-pipeline.md) |

## R3. Разработка

| Код | Название | Ур. | Д0/E | Статус | Файл |
|---|---|---|---|---|---|
| R3.1 | Цикл фичи | A | Д0 | `stub` | [R3.1-feature-cycle.md](R3.1-feature-cycle.md) |
| R3.2 | Малые изменения | A | Д0 | `stub` | [R3.2-small-changes.md](R3.2-small-changes.md) |
| R3.3 | Стиль, линтеры, типы | A | Д0 | `stub` | [R3.3-style-linters-types.md](R3.3-style-linters-types.md) |
| R3.4 | Обработка отказов | A | Д0 | `stub` | [R3.4-failure-handling.md](R3.4-failure-handling.md) |
| R3.5 | Гигиена веток и рабочих деревьев агентов | A | Д0 | `active` | [R3.5-branch-and-worktree-hygiene.md](R3.5-branch-and-worktree-hygiene.md) |
| R3.6 | Права и действия агента | A | Д0 | `draft` | [R3.6-agent-permissions-and-actions.md](R3.6-agent-permissions-and-actions.md) |
| R3.7 | Дублирование и абстракции | A | — | `stub` | [R3.7-duplication-and-abstractions.md](R3.7-duplication-and-abstractions.md) |

## R4. Качество

| Код | Название | Ур. | Д0/E | Статус | Файл |
|---|---|---|---|---|---|
| R4.1 | Пирамида тестов и обязательные ярусы на PR | A | Д0 | `active` | [R4.1-testing-pyramid.md](R4.1-testing-pyramid.md) |
| R4.2 | Гейт CI | A | Д0 | `stub` | [R4.2-ci-gate.md](R4.2-ci-gate.md) |
| R4.3 | Сторожа и мутации | A | Д0 | `active` | [R4.3-guards-and-mutations.md](R4.3-guards-and-mutations.md) |
| R4.4 | Код-ревью | A | Д0 | `stub` | [R4.4-code-review.md](R4.4-code-review.md) |
| R4.5 | Definition of Done | A | Д0 | `stub` | [R4.5-definition-of-done.md](R4.5-definition-of-done.md) |
| R4.6 | Evals LLM | A | E | `stub` | [R4.6-llm-evals.md](R4.6-llm-evals.md) |
| R4.7 | Мутационное тестирование | A | E | `stub` | [R4.7-mutation-testing.md](R4.7-mutation-testing.md) |

## R5. Поставка

| Код | Название | Ур. | Д0/E | Статус | Файл |
|---|---|---|---|---|---|
| R5.1 | Деплой | B | Д0 | `stub` | [R5.1-deploy.md](R5.1-deploy.md) |
| R5.2 | Миграции в проде | A | Д0 | `stub` | [R5.2-prod-migrations.md](R5.2-prod-migrations.md) |
| R5.3 | Приёмка на проде | A | — | `draft` | [R5.3-prod-acceptance.md](R5.3-prod-acceptance.md) |
| R5.4 | Откат | A | — | `stub` | [R5.4-rollback.md](R5.4-rollback.md) |

## R6. Эксплуатация

| Код | Название | Ур. | Д0/E | Статус | Файл |
|---|---|---|---|---|---|
| R6.1 | SLO и алерты | A | Д0 | `stub` | [R6.1-slo-and-alerts.md](R6.1-slo-and-alerts.md) |
| R6.2 | Телеметрия | A | Д0 | `stub` | [R6.2-telemetry.md](R6.2-telemetry.md) |
| R6.3 | Рунбуки | B | — | `stub` | [R6.3-runbooks.md](R6.3-runbooks.md) |
| R6.4 | Инциденты и постмортемы | A | — | `stub` | [R6.4-incidents-and-postmortems.md](R6.4-incidents-and-postmortems.md) |
| R6.5 | Бэкап и restore-тест | A | Д0 | `stub` | [R6.5-backup-and-restore-test.md](R6.5-backup-and-restore-test.md) |

## R7. Сессия и агенты

| Код | Название | Ур. | Д0/E | Статус | Файл |
|---|---|---|---|---|---|
| R7.1 | Оркестрация сессии | C | — | `stub` | [R7.1-session-orchestration.md](R7.1-session-orchestration.md) |
| R7.2 | Профили сессий | C | — | `draft` | [R7.2-session-profiles.md](R7.2-session-profiles.md) |
| R7.3 | Финал и передача уроков | C | — | `stub` | [R7.3-session-final-and-lessons.md](R7.3-session-final-and-lessons.md) |
| R7.4 | Харнес агента | A | Д0 | `stub` | [R7.4-agent-harness.md](R7.4-agent-harness.md) |
| R7.5 | Параллелизм агентов | A | Д0 | `draft` | [R7.5-agent-parallelism.md](R7.5-agent-parallelism.md) |

## Итого

**49 регламентов, из них 29 — день 0.** Сводная строка «45 регламентов, из них 27»
в источнике (`13_target_operating_model.md` §4) — ошибка счёта: в самих таблицах §4
перечислены 49 кодов (R0.1–R0.5, R1.1–R1.8, R2.1–R2.8, R3.1–R3.7, R4.1–R4.7,
R5.1–R5.4, R6.1–R6.5, R7.1–R7.5), из них с пометкой **Д0** — 29, с пометкой **E** — 5.
Каталог построен по множеству кодов, а не по сводке.

## Легенда

- **Уровень A** — портфель: правило общее для всех проектов, живёт здесь.
  **B** — проект: здесь лежит рамка, отклонения и раскладка — в репозитории проекта.
  **C** — сессия: правило исполняется скиллом сессии (`orchestrate` и профили).
- **Д0** — регламент обязателен на день 0 проекта (29 из 49). **E** — включается
  в фазе Expand (5). «—» — по мере надобности.
- **Статус** — состояние самого регламента, не проекта:
  - `active` — содержание написано и им можно пользоваться как есть;
  - `draft` — содержание есть, но закрывает границы частично (источник назван
    во фронтматтере `sources`);
  - `stub` — имя, границы и предотвращаемая ошибка; содержания нет.
  Четвёртое состояние — `retired`: регламент отменён, файл остаётся со ссылкой
  на заменивший.

## R0.4: урок → регламент в той же сессии

Урок, полученный в сессии, **в той же сессии** становится строкой регламента или
гейтом — либо не считается усвоенным. Память сессии привязана к каталогу проекта
и в следующем проекте не существует: villas дошёл до 11 уроков из 18, живущих
только в памяти.

Порядок: (1) найти регламент по коду в таблице выше; (2) дописать урок разделом
в его файл, сохранив ключевую формулировку, по которой урок ищется grep'ом;
(3) поднять статус (`stub` → `draft` → `active`); (4) в файле памяти, откуда
урок перенесён, оставить строку `закреплено: ai_tools R<n>.<m>` — файл памяти
не удаляется.

