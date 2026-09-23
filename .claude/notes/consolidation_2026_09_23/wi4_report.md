# WI-4 — template «день 0» `templates/project-day0/`

Ветка `feat/wi4-day0-template`, worktree `.claude/worktrees/wi4-day0-template`. Не пушилось.

## Главное расхождение с ТЗ: пунктов 29, а не 27

ТЗ и §4 villas говорят «27 пунктов Д0». В самом §4
(`13_target_operating_model.md`) пометку **Д0** несут **29** регламентов — пересчёт строк
таблиц, не оценка:

```
grep -cE '^\| R[0-7]\.[0-9] \*\*Д0\*\*' 13_target_operating_model.md  ->  29
```

Итоговая строка §4 («45 регламентов, из них 27 — день 0») сбита в обеих величинах: всего
регламентов в таблицах не 45, а **49** (R0×5, R1×8, R2×8, R3×7, R4×7, R5×4, R6×5, R7×5).
Расхождение 49−45 = 4 и 29−27 = 2 — это ошибка счёта в сводке, а не другой набор пунктов.

Решение: чек-лист построен по **множеству пометок Д0**, а не по числу из сводки, потому
что множество перечислимо и проверяемо, а число — нет. В `DAY0.md` 29 пунктов.
**Владельцу решить:** поправить сводку §4 villas (29/49) или сознательно выкинуть два
пункта из дня 0 — тогда нужны коды и ADR-обоснование.

Коды в `DAY0.md` (ровно множество Д0 из §4):

```
R0.1 R0.2 R0.3 R0.4
R1.1 R1.2
R2.1 R2.2 R2.3 R2.4 R2.5
R3.1 R3.2 R3.3 R3.4 R3.5 R3.6
R4.1 R4.2 R4.3 R4.4 R4.5
R5.1 R5.2
R6.1 R6.2 R6.5
R7.4 R7.5
```

## Структура

```
templates/project-day0/
├── .claude/notes/.gitkeep
├── .github/workflows/gate.yml
├── .gitignore
├── CLAUDE.md
├── DAY0.md
├── README.md
├── data/.gitkeep
├── docs/
│   ├── adr/0001-template.md
│   ├── adr/README.md
│   └── testing.md
├── scripts/day0_check.py
├── src/.gitkeep
└── tests/test_day0_check.py
```

`.secrets/` в git не попадает: каталога в шаблоне нет, строка `.secrets/` стоит в
`.gitignore` до появления файлов, README велит создать его руками (п. 3).

## Критерии готовности — вывод команд

```
$ wc -l CLAUDE.md
43 CLAUDE.md                                   # предел 60

$ grep -c '^- \[ \] R' DAY0.md
29                                             # см. раздел о расхождении выше

$ grep -cE 'paths:|continue-on-error' .github/workflows/gate.yml
0

$ python scripts/day0_check.py
  [ ] R0.1 - Конституция проекта
  ... (29 строк) ...
  [ ] R7.5 - Параллелизм агентов
29 items total
29 open items
exit=1
```

Линтеры и типы (venv в scratchpad: ruff 0.16.8, mypy 2.3.1, pytest 9.0.2; локальный
Python 3.10.11, в гейте — 3.12):

```
$ ruff check .
All checks passed!

$ mypy --strict scripts/day0_check.py
Success: no issues found in 1 source file

$ pytest -q --strict-markers
..........                                                               [100%]
10 passed in 1.12s
```

Копия `DAY0.md` со всеми `[x]` даёт exit 0 — это тесты `test_all_checked_passes` и
`test_uppercase_checkbox_counts_as_closed`; тесты гоняют реальный call-site
(`python scripts/day0_check.py` через `subprocess`), а не только импорт функции.

## Доказательство мутацией

Мутация в `scripts/day0_check.py`, `collect()`:

```python
-            match.group("body"), match.group("mark") != " ", project_root
+            match.group("body"), True, project_root
```

то есть «любой `- [ ]` считаем закрытым». Результат:

```
$ pytest -q --strict-markers
4 failed, 6 passed
FAILED test_template_checklist_is_fully_open       - шаблон объявлен пройденным
FAILED test_explicit_path_argument                 - то же при явном пути
FAILED test_skip_without_adr_stays_open            - пропуск без ADR стал закрытым
FAILED test_template_checklist_matches_the_file    - парсер «потерял» все открытые

$ python scripts/day0_check.py
29 items total
all 29 items closed
exit=0        # вместо 1 — гейт пропустил бы пустой проект в прод
```

Мутация откачена, после отката `ruff`/`mypy --strict`/`pytest` зелёные (вывод выше).
Первая попытка мутации была негодной: комментарий `# MUTATION` в конце строки аргументов
съел `project_root`, и тесты падали на `TypeError`, а не на поведении. Переделано —
падение поведенческое.

## Решения, принятые по ходу

- **Примеры в ``` игнорируются.** Преамбула `DAY0.md` показывает синтаксис `[skip: ADR-nnnn]`
  живой строкой; парсер считал её 30-м пунктом. Парсер учит границы fenced-блоков
  (тест `test_fenced_examples_are_not_checklist_items`), а пример в преамбуле дополнительно
  сдвинут отступом, чтобы и наивный `grep '^- \[ \] R'` давал ровно 29.
- **Вывод скрипта — UTF-8 принудительно** (`force_utf8()`): на Windows-консоли cp1251
  кириллические названия пунктов выходили мусором. В гейте (ubuntu) разницы нет.
- **Корень проекта для поиска ADR** — каталог, где лежит сам `DAY0.md`, а не cwd: скрипт
  корректен и при запуске из другого каталога, и на копии чек-листа во временной папке.
- **Ссылки на регламенты — абсолютные на GitHub** плюс код R…, как велит ТЗ: WI-1 строит
  `docs/regulations/` параллельно, и имён файлов ещё нет.
- Коды регламентов в `docs/regulations/README.md` (ai_tools) пока не заведены — ссылки
  ведут на README каталога и станут точными, когда WI-1 расставит якоря по кодам.

## Что НЕ сделано (осознанно)

- **Код скелета не пишется** — граница ТЗ. Пункты `R2.3` (кодоген контракта), `R2.5`
  (реестр флагов), `R3.4` (`best_effort()`) в `DAY0.md` есть и остаются открытыми; в
  преамбуле сказано, что это нормальное состояние свежего проекта.
- **`pyproject.toml` в шаблон не положен**: `ruff` и `mypy` проходят на настройках по
  умолчанию, а конфигурация линтеров — часть пункта R3.3, который проект закрывает сам под
  свой стек (Python-only шаблон не должен навязывать раскладку фронтенду).
- **`gate.yml` не прогонялся в GitHub Actions** — не пушили; проверены только содержимое
  (нет `paths:`, нет `continue-on-error`, один джоб) и то, что каждая его команда зелёная
  локально, кроме последней, которая обязана быть красной.
- `docs/registry.md` (реестр параметров и флагов) в шаблоне не заведён — это артефакт
  пункта R2.5, а не скелета; `CLAUDE.md` и `DAY0.md` на него ссылаются как на то,
  что проект создаёт.
- `.secrets/` не создан намеренно (иначе попал бы в git пустым каталогом или `.gitkeep`).

## Коммиты

- `6d3e8b7` — `templates/project-day0/**` (13 файлов).
- отчёт — следующим коммитом.
