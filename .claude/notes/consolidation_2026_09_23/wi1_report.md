# WI-1 — каталог регламентов `docs/regulations/`: отчёт

Дата: 2026-09-23 · Ветка: `feat/wi1-regulations` · Worktree:
`.claude/worktrees/wi1-regulations` (не пушится, не удаляется).

Источники: villas `.claude/notes/bug_stream_root_causes_2026_09_22/13_target_operating_model.md`
(§2–§4, §7, §9) и `09_regulations_inventory.md` (таблицы A–D), память villas (18 уроков),
`docs/regulations/testing-pyramid.md`, villas `docs/trello-board-workflow.md` + `CLAUDE.md`,
villas `docs/specs/README.md`.

---

## 1. Расхождение с ТЗ: регламентов не 45, а 49

Каталог §4 в `13_target_operating_model.md` подводит итог «**45 регламентов, из них 27 —
день 0**». Пересчёт строк самой таблицы даёт другое:

```
$ grep -cE '^\| R[0-7]\.[0-9]+' 13_target_operating_model.md
49
$ grep -E '^\| R[0-7]\.[0-9]+' 13_target_operating_model.md | grep -c 'Д0'
29
$ grep -E '^\| R[0-7]\.[0-9]+' 13_target_operating_model.md | grep -c '\*\*E\*\*'
5
```

Коды по группам: R0 — 5, R1 — 8, R2 — 8, R3 — 7, R4 — 7, R5 — 4, R6 — 5, R7 — 5 = **49**.
Пропусков в нумерации нет (R0.1…R0.5, R1.1…R1.8, …, R7.1…R7.5).

**Решение:** заведены все 49 кодов, которые реально перечислены в §4. Ни один не выдуман
и ни один не выброшен. **Критерий скорректирован оркестратором 23.09.2026: «45 из ТЗ
скорректировано на 49, Д0 27 → 29».** Истина — множество кодов в таблицах §4
(R0.1–R0.5, R1.1–R1.8, R2.1–R2.8, R3.1–R3.7, R4.1–R4.7, R5.1–R5.4, R6.1–R6.5,
R7.1–R7.5); число «45/27» в сводной строке §4 и в ТЗ — ошибка счёта. В `README.md`
внизу стоит строка «49 регламентов, из них 29 — день 0».

Оговорка по букве команды критерия: `ls docs/regulations/R*.md | wc -l` даёт **50**,
потому что шаблон `R*` матчит и `README.md`. Регламентов ровно 49 —
`ls docs/regulations/R[0-9]*.md | wc -l` = 49.

## 2. 18 уроков памяти — список подтверждён

В `09_regulations_inventory.md`, раздел B, ровно **18** уроков (таблица «# 1–18», итог
раздела: «18 уроков-правил»). Расхождений с ТЗ нет. Все 18 перенесены.

## 3. Урок памяти → файл R*.md → ключевая фраза для grep

| # | Урок памяти | Регламент | Файл | Ключевая фраза для grep |
|---|---|---|---|---|
| 1 | `feedback_no_sdlc` | R7.2 | `R7.2-session-profiles.md` | `через SDLC-скиллы` |
| 2 | `feedback_artifacts_in_repo` | R0.2 | `R0.2-repo-structure-and-template.md` | `Всё, что относится к проекту, хранится в проекте` |
| 3 | `repo_structure_convention` | R0.2 | `R0.2-repo-structure-and-template.md` | `полезная нагрузка, код по папкам` |
| 4 | `feedback_measure_before_code` | R1.1 | `R1.1-definition-of-ready.md` | `замер ДО кода` |
| 5 | `feedback_develop_it` | R7.5 | `R7.5-agent-parallelism.md` | `ревью и правка — строго по очереди` |
| 6 | `feedback_questions_in_session` | R1.5 | `R1.5-owner-decisions-and-questions.md` | `только решённая работа` |
| 7 | `lesson_green_helper_not_green_feature` | R4.1 | `R4.1-testing-pyramid.md` | `новая метрика окупается в том же ревью` |
| 8 | `feedback_orphaned_tests_gate` | R4.3 | `R4.3-guards-and-mutations.md` | `какой ИМЕННО джоб его исполнит` |
| 9 | `gh_actions_api_filters_lie` | R3.6 | `R3.6-agent-permissions-and-actions.md` | `соврал в обе стороны` |
| 10 | `feedback_probe_permissions_not_actions` | R3.6 | `R3.6-agent-permissions-and-actions.md` | `это не проверка, это действие` |
| 11 | `feedback_verify_branch_shared_checkout` | R3.5 | `R3.5-branch-and-worktree-hygiene.md` | `сверка состава мержа` |
| 12 | `feedback_preview_start_ignores_worktree` | R5.3 | `R5.3-prod-acceptance.md` | `Первым делом класть маркер` |
| 13 | `feedback_solve_findings_now` | R1.2 | `R1.2-defect-policy-class-or-close.md` | `решать её сейчас, в этой же сессии` |
| 14 | `board_priority_order` | R1.6 | `R1.6-board-columns-codes-duplicates.md` | `полнота и качество данных` |
| 15 | `feedback_measure_where_the_check_runs` | R1.1 | `R1.1-definition-of-ready.md` | `по МЕСТУ исполнения и по ПОПУЛЯЦИИ` |
| 16 | `feedback_substring_assertions_not_guards` | R4.3 | `R4.3-guards-and-mutations.md` | `утверждения на подстроке` |
| 17 | `feedback_killed_agents_armed_mutations` | R3.5 | `R3.5-branch-and-worktree-hygiene.md` | `вооружённую мутацию` |
| 18 | `write_path_fix_needs_reextraction` | R5.3 | `R5.3-prod-acceptance.md` | `путь записи или чтения` |

Обоснование спорных привязок (уроки, которые касаются двух регламентов):
- №12 `preview_start` — к R5.3 (приёмка), а не к R3.5: так его классифицирует
  `09_regulations_inventory.md` §C («Приёмка на проде: уроки №12, 15, 18»). Общий корень
  с R3.5 назван ссылкой внутри файла.
- №5 `feedback_develop_it` — к R7.5 (параллелизм): содержательная часть урока это
  сериализация доступа к worktree, именование в общем scratchpad, ≤ 1 ssh на хост и
  миграции параллельных веток. R3.1 (цикл фичи) остаётся `stub`: его источник — скилл
  `develop-it`, который переносится в WI-2, а не память.
- №9 `gh_actions_api_filters_lie` — к R3.6 вторым разделом: урок о том, что и читающий
  запрос умеет соврать; в паре с №10 он закрывает «как агент узнаёт правду о мире».

## 4. Счётчики

| Величина | Значение |
|---|---|
| Регламентов в каталоге (файлов `R<n>.<m>-*.md`) | **49** |
| Строк каталога в `README.md` | **49** |
| Перенесено уроков памяти | **18 / 18** |
| Регламентов со статусом `active` | **5** (R1.5, R1.6, R3.5, R4.1, R4.3) |
| Регламентов со статусом `draft` | **9** (R0.2, R0.4, R1.1, R1.2, R1.4, R3.6, R5.3, R7.2, R7.5) |
| Регламентов со статусом `stub` | **35** |
| Файлов памяти villas с отметкой `закреплено: ai_tools R…` | **18** |
| Д0-регламентов | 29 · **E** — 5 |

`testing-pyramid.md` перенесён `git mv` в `R4.1-testing-pyramid.md` (история файла
сохранена), получил фронтматтер и раздел 10 с уроком №7; старого имени в каталоге нет.

## 5. Вывод команд критериев

```
$ grep -cE '^\| R[0-7]\.[0-9]' docs/regulations/README.md
49                       # скорректировано: в ТЗ было 45 — см. §1 отчёта
$ ls docs/regulations/R[0-9]*.md | wc -l
49
$ ls docs/regulations/R*.md | wc -l
50                       # шаблон R* матчит и README.md; регламентов 49
$ ls docs/regulations/ | grep -c '^testing-pyramid.md$'
0
$ grep -c 'Регламент' docs/regulations/README.md
3                        # кодировка UTF-8 не побита
$ grep -c '49 регламентов, из них 29 — день 0' docs/regulations/README.md
1
$ grep -rl 'закреплено: ai_tools R' <memory villas> | wc -l
18
$ python — ссылки README → файлы
links: 49 missing: []
$ python — фронтматтер (code/status) ↔ имя файла ↔ строка README
frontmatter/README mismatches: []
```

Проверка «каждый урок ровно в одном файле R*.md» (эквивалент
`grep -rl "<фраза>" docs/regulations/R*.md | wc -l` = 1 для всех 18 фраз):

```
feedback_no_sdlc                           R7.2 OK count=1 «через SDLC-скиллы»
feedback_artifacts_in_repo                 R0.2 OK count=1 «Всё, что относится к проекту, хранится в проекте»
repo_structure_convention                  R0.2 OK count=1 «полезная нагрузка, код по папкам»
feedback_measure_before_code               R1.1 OK count=1 «замер ДО кода»
feedback_develop_it                        R7.5 OK count=1 «ревью и правка — строго по очереди»
feedback_questions_in_session              R1.5 OK count=1 «только решённая работа»
lesson_green_helper_not_green_feature      R4.1 OK count=1 «новая метрика окупается в том же ревью»
feedback_orphaned_tests_gate               R4.3 OK count=1 «какой ИМЕННО джоб его исполнит»
gh_actions_api_filters_lie                 R3.6 OK count=1 «соврал в обе стороны»
feedback_probe_permissions_not_actions     R3.6 OK count=1 «это не проверка, это действие»
feedback_verify_branch_shared_checkout     R3.5 OK count=1 «сверка состава мержа»
feedback_preview_start_ignores_worktree    R5.3 OK count=1 «Первым делом класть маркер»
feedback_solve_findings_now                R1.2 OK count=1 «решать её сейчас, в этой же сессии»
board_priority_order                       R1.6 OK count=1 «полнота и качество данных»
feedback_measure_where_the_check_runs      R1.1 OK count=1 «по МЕСТУ исполнения и по ПОПУЛЯЦИИ»
feedback_substring_assertions_not_guards   R4.3 OK count=1 «утверждения на подстроке»
feedback_killed_agents_armed_mutations     R3.5 OK count=1 «вооружённую мутацию»
write_path_fix_needs_reextraction          R5.3 OK count=1 «путь записи или чтения»

строка «закреплено: ai_tools R…» — во всех 18 файлах памяти: OK
R-файлов (без README): 49 · статусы: stub 35, draft 9, active 5
итог: ВСЕ КРИТЕРИИ ЗЕЛЁНЫЕ
```

Ссылки README → файлы: 49 ссылок, отсутствующих файлов 0. Фронтматтер: у всех 49 файлов
есть `code:` и `status:`, код совпадает с именем файла и со строкой README.

Скрипты проверки и генерации — в scratchpad сессии (`gen_regs.py`, `pin_memory.py`,
`check.py`); в репозиторий не кладутся: одноразовая обвязка.

## 6. Что НЕ сделано и почему

- **Содержание 35 stub-регламентов не написано** — граница ТЗ: только имя, границы,
  предотвращаемая ошибка, строка «не написано; см. R0.4».
- **R0.4 сделан `draft`, а не `stub`** (отступление от буквы ТЗ). Его содержание уже
  существует в §2/§4 источника и в легенде README — три уровня A/B/C, состояния
  регламента, правило «урок → регламент в той же сессии». Stub со строкой
  «не написано; см. R0.4» в файле самого R0.4 был бы самоссылкой.
- **R3.1 (цикл фичи), R4.4 (код-ревью), R7.1/R7.3 (оркестрация, финал)** остались
  `stub`, хотя §4 помечает их «скилл»: их содержание живёт в скиллах `orchestrate` /
  `develop-it`, перенос которых — WI-2/WI-3, а не эта задача.
- **R1.4 — `draft` с пометкой «переписать»**: перенесён действующий SDD-источник villas
  целиком, с явной пометкой, что критерий готовности сужается до ~30 операций под SLO
  (решение владельца 23.09). Сужение не выполнено — это правка villas (WI-5) и R6.2.
- **Корневой `README.md` репозитория не тронут** (его правит оркестратор).
- **Память villas**: в 18 файлах добавлена **одна строка** в конец, ничего не удалено
  и не переписано.
