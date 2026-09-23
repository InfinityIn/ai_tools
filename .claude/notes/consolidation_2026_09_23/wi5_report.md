# WI-5 — подключение villas к каталогу регламентов ai_tools

Дата: 2026-09-23. Репозиторий: `F:/projects/villas/code/villas`.
Ветка: `chore/regulations-link`, коммит `ba0691df`, запушена в origin.
**PR не создан** — токен не имеет права (см. «Что НЕ сделано»).

## Что сделано

Дерево villas было чистым, `main` совпадал с `origin/main` (`68563f0c`) —
работал обычной веткой от main, без worktree.

### 1. `CLAUDE.md` (43 → 66 строк, +69/−23)

| Было | Стало |
|---|---|
| — | Шапка: ссылка на [каталог регламентов ai_tools](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/README.md) + строка-ссылка на `docs/agent-traps.md` |
| п.1 блока доски: «**Правило нуля**: во время спринта в Sprint ничего не создаётся… находка → **Inbox** одной строкой» | Новый раздел «**Находка: „класс или закрыть“**» со ссылкой на R1.2: находка закрывает класс (карточка с **названным сторожем**), либо чинится в этой же сессии, либо не заводится вовсе; экземпляр без класса карточкой не становится |
| Блок доски: 7 пунктов свода (обмен по P1, набор спринта, дубль, вопросы владельцу, кто ходит к Trello, метрика финала) + delivery/discovery | Ссылка на R1.6 (всё перечисленное там) + 3 строки отклонений villas |
| SDD п.3: «Критерий готовности включает телеметрию: **каждая** новая/изменённая операция отдаёт `op="<ID>"`…» | Ссылка на R6.2 + «телеметрия только под SLO (~30 операций), решение владельца 23.09.2026; сплошная разметка всех операций реестра отменена». DoD сохранён, но только **для операций под SLO** |
| — | Новый раздел «**Тесты**» → ссылка на R4.1 (две оси, обязательные ярусы на PR, сторож без мутационного счёта — не сторож) |

Остальное (реестр SDD, пункты 1, 2, 4, 5, 6) не тронуто.

### 2. Три строки отклонений доски (villas vs R1.6)

Сравнил блок `CLAUDE.md` + `docs/trello-board-workflow.md` с R1.6. Правила
потока совпадают почти дословно (R1.6 из villas и собран) — отклонения не
в правилах, а в привязке к проекту и в одном протухшем пункте:

1. **Трекер — Trello**; id колонок, именование `[КОД] Название` с префиксами
   проекта (CB/OPS/SEC/QA/DOC/PAY) и живой порядок доски — в
   `docs/trello-board-workflow.md` и в памяти (`trello_board.md`,
   `board_priority_order.md`). R1.6 — уровень B, конкретная доска в нём не живёт.
2. **Ёмкость 10–12 карточек на сессию и формулы срока** — замер villas
   08–09.2026, свойство этого проекта, а не норма регламента.
3. **Пункт 1 в `docs/trello-board-workflow.md`** («во время спринта любая
   находка → Inbox одной строкой») **отменён** решением владельца 23.09.2026;
   действует R1.2. Документ доски сам не переписан — это за границей WI-5.

### 3. `docs/agent-traps.md` (новый, 80 строк)

Перенесён содержательный текст из `.claude/notes/villas_traps_for_wi5.md`
(`.claude/notes/` в villas в `.gitignore` — файл был вне отслеживания).
Служебные разделы «происхождение/куда девать» свёрнуты в одну сноску внизу.
Пять ловушек, каждая с привязкой к регламенту: Alembic (R2.4/R5.2), worktree
и `PYTHONPATH` (R3.5), `.env`/`DOTENV_PATH`/дев-БД (R2.5), секреты и живые
compose (R0.5/R5.1), `fb-loop` (R3.6).

**Проверка актуальности чтением (не действием), 23.09.2026 — всё подтвердилось:**

| Утверждение | Доказательство |
|---|---|
| `load_dotenv(override=True)` | `src/core/villas_core/config.py:56` — `load_dotenv(_resolve_dotenv(), override=True)`; то же в `src/fb-scraper/villas_fb_scraper/config.py:37` |
| `DOTENV_PATH` жив | `cicd/ci_parser_suite.sh:83` (`export DOTENV_PATH="$CI_ENV"`), сторож `src/core/villas_core/testing/db_guard.py`, ~40 тестов в докстрингах |
| Дев-БД 5434 | `cicd/compose.local.yml:36` — `"127.0.0.1:5434:5432"` (комментарий на :32 объясняет, почему не 5432/5433); `.env.local.example:10–11` |
| `villas_core` editable резолвится в основной checkout | `site-packages/_villas_core.pth` (+ `_villas_api_*.pth`, `_editable_impl_villas_parser.pth`); `import villas_core` отдаёт `F:\projects\villas\code\villas\src\core\villas_core\__init__.py` |
| Секреты в `.secrets/`, ключ `~/.ssh/claude_deploy` | `.gitignore` содержит `.secrets/`; каталог существует (`gh_pat`, `prod.env`, `trello_*`, `villas_breakglass`); `~/.ssh/claude_deploy` существует |
| Миграция отдельным пушем | `.github/workflows/migrate.yml`: `push: branches:[main], paths: src/core/alembic/versions/**` — отдельный джоб |
| Тесты ядра не передеплоивают прод | сторож `cicd/tests/test_ops110_core_tests_do_not_redeploy_prod.py` существует |

Пометок «(не подтверждено 23.09)» в файле нет — не понадобились.

### 4. Память villas `MEMORY.md`

В раздел «Правила работы (читать первыми)» первой строкой добавлено:

```
- Регламенты разработки — [каталог ai_tools `docs/regulations`](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/README.md) (49 R-кодов); уроки памяти помечены «закреплено: ai_tools R…»
```

Ничего не удалено; указатели на `feedback_*`/`lesson_*` на месте.
В ТЗ значилось 45 R-кодов — в каталоге фактически **49** (`ls docs/regulations/R*.md` = 49),
в строку памяти поставил фактическое число.

### 5. Проверка перед пушем: CI не деплоит с ветки

Просмотрел все 28 воркфлоу в `.github/workflows/`. **Ни один `push:`-триггер
не срабатывает на ветке, кроме `main`** — у всех явный `branches: [main]`.
На открытие PR сработают только гейты без деплоя: `ci-guards.yml`
(`pull_request`, без `paths`) и `security-scan.yml` (`pull_request`).
Изменены только markdown-файлы; `paths`-фильтры деплой-воркфлоу их не ловят.
Прод не затрагивается.

## Вывод критериев (п.5 задания)

```
grep -c  "ai_tools"     CLAUDE.md  = 6      (≥ 1 ✔)
grep -ci "правил. нуля" CLAUDE.md  = 0      (= 0 ✔)
grep -c  "правило нуля" CLAUDE.md  = 0      (= 0 ✔)
docs/agent-traps.md существует             ✔  (80 строк)
упомянут в CLAUDE.md (grep -c agent-traps) = 1  ✔
MEMORY.md grep -c "ai_tools"        = 3     (≥ 1 ✔)
ветка запушена: origin/chore/regulations-link = ba0691df  ✔
PR создан                                   ✘ — см. ниже
```

## Что НЕ сделано

**PR не создан: у PAT нет права на pull requests.**

`F:/projects/villas/code/villas/.secrets/gh_pat` — **fine-grained** токен
(ответ `/user` не отдаёт `x-oauth-scopes`). На `InfinityIn/villas` он имеет
`admin/maintain/push/triage/pull` по Contents, но любое обращение к
pull-requests API отвечает 403 `Resource not accessible by personal access token`:

```
POST /repos/InfinityIn/villas/pulls   → 403
GET  /repos/InfinityIn/villas/pulls   → 403
GET  /repos/InfinityIn/villas/issues  → 403
```

Это не разовый сбой, а отсутствующее разрешение токена — касается всех
будущих PR через API в villas (и, вероятно, в ai_tools тоже: токен один).
Пароль из Windows Credential Manager вытаскивать не стал — он выдан для
git-push, не для API, и в задании как API-кредом не назван.

**Два способа закрыть (нужно владельцу):**

1. В настройках токена (Developer settings → Fine-grained tokens → этот токен →
   Repository permissions) выдать **Pull requests: Read and write**. После этого
   PR создаётся одной командой — черновик тела PR ниже.
2. Или открыть PR руками:
   <https://github.com/InfinityIn/villas/pull/new/chore/regulations-link>

Ветка уже на origin, мержить её **нельзя без владельца** (`main` villas = прод).

**Черновик PR** (title ASCII, body английский, последняя строка — обязательная):

> **Title:** `chore: link CLAUDE.md to ai_tools regulations catalog (R1.2/R1.6/R6.2/R4.1)`
>
> Links villas `CLAUDE.md` to the shared regulations catalog in
> [InfinityIn/ai_tools `docs/regulations/`](https://github.com/InfinityIn/ai_tools/blob/main/docs/regulations/README.md).
> Rules common to all projects are linked, not copied; only villas-specific deviations stay here.
>
> **Changes**
>
> - **"Zero rule" replaced by "class or close" (R1.2)** — owner decision 2026-09-23. A finding either
>   closes a *class* of defects (card with a named guard: the test/gate/linter that stops it recurring),
>   or is fixed in the same session, or is not filed at all. An instance without a class never becomes a card.
> - **Board block -> link to R1.6** plus 3 lines of villas deviations: Trello and this project's card
>   codes; capacity 10-12 cards/session is a villas measurement, not a norm; item 1 of
>   `docs/trello-board-workflow.md` is cancelled and superseded by R1.2.
> - **Telemetry -> R6.2** plus "only under SLO (~30 operations)", owner decision 2026-09-23. Blanket
>   `op=` labelling of every registry operation is cancelled; the DoD stays for operations under SLO.
> - **New "Tests" block -> R4.1** (testing pyramid, mandatory tiers on PR).
> - **New `docs/agent-traps.md`** — project traps for agents (Alembic single head, worktree not getting
>   its own `villas_core`, repo-root `.env` overriding test env / dev DB on 5434, secrets and the live
>   compose location, `fb-loop` single-session rule). Every trap re-verified by reading the code on
>   2026-09-23. Linked from `CLAUDE.md`. The text used to live in the `develop-it` skill; it cannot go
>   to `ai_tools`, which is public.
>
> **Production is untouched.** Markdown only; every deploy workflow triggers on `push: branches: [main]`,
> so pushing this branch deploys nothing. **Do not merge without the owner** — `main` of villas is prod.
>
> Part of the ai_tools consolidation session (WI-5), 2026-09-23.
>
> 🤖 Generated with [Claude Code](https://claude.com/claude-code)

**Сознательно за границей WI-5** (не дефекты, а следующая работа):

- `docs/trello-board-workflow.md` всё ещё содержит отменённое правило в п.1 —
  в `CLAUDE.md` это названо явно (отклонение 3), но сам документ не переписан.
- Файлы памяти villas не получили строк «закреплено: ai_tools R…» — это WI-1,
  не WI-5; строка в `MEMORY.md` про пометку уже стоит.
- `docs/testing.md` с раскладкой ярусов villas (его требует R4.1) не заведён —
  в `CLAUDE.md` стоит только ссылка на регламент.
- Trello не тронут, прод не тронут, PR не смержен.
