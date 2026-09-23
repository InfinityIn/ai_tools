# Справочники

Справочники — это не скиллы. Они не устанавливаются в `~/.claude/skills/` и
ничего не запускают: это описание того, **что должно быть на выходе** этапа
работы. Как вести сессию — в профильных скиллах `src/process/`.

Источник — бывшие скиллы `sdlc-*` (удалены из `~/.claude/skills` 2026-09-23);
справочники не устанавливаются как скиллы.

## SDLC: артефакты этапов — `sdlc/`

| Этап | Справочник | Рабочий контур | Регламенты |
|---|---|---|---|
| Сбор требований | [sdlc/requirements.md](sdlc/requirements.md) | `develop-it` · корпоративный контур частично | R1.1, R1.4, R1.5 |
| Архитектура | [sdlc/architecture.md](sdlc/architecture.md) | `develop-it`, `research-it` · корпоративный контур частично | R2.1, R2.2, R2.6 |
| Системный анализ | [sdlc/system-analysis.md](sdlc/system-analysis.md) | `develop-it` | R1.4, R2.3, R2.4 |
| Разработка (код) | [sdlc/development.md](sdlc/development.md) | `develop-it` | R3.1–R3.4 |
| Разработка: бэкенд | [sdlc/development-backend.md](sdlc/development-backend.md) | `develop-it` | R2.3, R2.4, R3.4, R5.2 |
| Разработка: фронтенд | [sdlc/development-frontend.md](sdlc/development-frontend.md) | `develop-it` | R2.3, R3.1, R5.3 |
| Проверка кода | [sdlc/code-review.md](sdlc/code-review.md) | `develop-it` | R4.4, R4.3, R3.2 |
| Сборка (CI/CD) | [sdlc/build.md](sdlc/build.md) | `develop-it` | R4.2, R5.1 |
| Тест-документация | [sdlc/test-docs.md](sdlc/test-docs.md) | `develop-it`, `analyze-it` · **корпоративный контур** | R1.1, R4.1 |
| Тест-дизайн | [sdlc/test-design.md](sdlc/test-design.md) | `develop-it` · **корпоративный контур** | R4.1, R4.3 |
| Тестирование (прогон) | [sdlc/testing.md](sdlc/testing.md) | `develop-it` | R4.1, R4.3, R5.3 |
| Эксплуатация | [sdlc/operations.md](sdlc/operations.md) | `analyze-it` | R6.1–R6.4 |
| Заведение задачи | [sdlc/new-feature.md](sdlc/new-feature.md) | `develop-it` · корпоративный контур частично | R1.4, R0.4, R3.5 |
| Продолжение задачи | [sdlc/continue-feature.md](sdlc/continue-feature.md) | `develop-it` · корпоративный контур частично | R1.4, R7.4 |
| Сквозной прогон | [sdlc/full.md](sdlc/full.md) | `develop-it` | R1.4, R3.1, R4.5 |

Коды регламентов раскрываются в [../../docs/regulations/README.md](../../docs/regulations/README.md).

### Приложения (шаблоны артефактов)

- [sdlc/test-design/test-cases-csv-format.md](sdlc/test-design/test-cases-csv-format.md)
  — формат экспорта тест-кейсов в CSV (столбцы, экранирование, импорт в TMS).
- [sdlc/development/corporate-code-standard.md](sdlc/development/corporate-code-standard.md)
  — корпоративный стандарт кода и структуры сервисов.
- [sdlc/code-review/corporate-code-review-policy.md](sdlc/code-review/corporate-code-review-policy.md)
  — корпоративный регламент проверки кода.

## Как читать

- **Рабочий контур** — профильный скилл из `src/process/`, который ведёт работу.
  Справочник отвечает на вопрос «что на выходе», скилл — «как дойти».
- **Корпоративный контур** — этап опирается на внешние системы (Jira,
  Confluence, Figma, система управления тестированием). Вне такой среды этап
  работает по локальным материалам; что именно теряется — описано в разделе
  «Корпоративный контур» каждого справочника.
- Три последних справочника (`new-feature`, `continue-feature`, `full`) описывают
  каркас задачи и порядок этапов. Сам процесс ведёт `develop-it` в связке со
  спецификацией фичи (R1.4).
