# Регламент разработки

Корпоративный стандарт написания кода и структуры проектов команды —
приложение к справочнику `../development.md` и `../development-backend.md`.
Применяется, только если проект работает в этом корпоративном контуре.
Источники (Confluence):

- [Соглашение о написании кода на C#](https://cfl.digtp.com/pages/viewpage.action?pageId=305612563)
- [Правила и соглашения наименования объектов C#](https://cfl.digtp.com/pages/viewpage.action?pageId=305612568)
- [Структура класса C#](https://cfl.digtp.com/pages/viewpage.action?pageId=305612677)
- [Типовая структура сервиса](https://cfl.digtp.com/pages/viewpage.action?pageId=309388158)
- [Типовая структура UseCases](https://cfl.digtp.com/pages/viewpage.action?pageId=309388161)
- [Подход к разделению разработки ЕХ–СГК](https://cfl.digtp.com/pages/viewpage.action?pageId=378922463)

> Импортировано из Confluence 2026-06-18. При расхождении — приоритет у Confluence.

---

## 1. Базовые принципы

Код соответствует соглашению о написании кода C#, стандартам чистого кода и принципам:

- **Least Surprise** — выбирать наиболее очевидное решение, не сбивать с толку других.
- **KISS** — наиболее простое решение задачи.
- **YAGNI** — не писать код «на будущее», решать текущую задачу.
- **DRY** — не дублировать код (с учётом «правила трёх»).
- **SOLID** — SRP, OCP, LSP, ISP, DIP.

## 2. Общие положения

- За основу взяты [C# Style Guide (Google)](https://google.github.io/styleguide/csharp-style.html) и [рекомендации Microsoft](https://learn.microsoft.com/ru-ru/dotnet/csharp/fundamentals/coding-style/coding-conventions); именование — по [рекомендациям Microsoft](https://learn.microsoft.com/ru-ru/dotnet/csharp/fundamentals/coding-style/identifier-names).
- Соблюдение требований обеспечивается через EditorConfig.

## 3. Форматирование

- Отступ — четыре пробела; согласованное выравнивание.
- Длина строки — до 150 символов.
- Скобки — стиль Allman (открывающая и закрывающая на своих строках, по уровню отступа).

### Организация файла

- `using` — вверху, до namespace; порядок алфавитный, `System.*` всегда первыми.
- `namespace` — в одну строку (стандарт .NET 6+).
- Порядок модификаторов: `public, private, protected, internal, static, extern, new, virtual, abstract, sealed, override, readonly, unsafe, volatile, async`.
- Один файл — один класс/тип; имя файла совпадает с именем основного класса (`MyClass.cs`); имена файлов и каталогов — **PascalCase**.

## 4. Наименование

Краткая сводка: классы/методы/перечисления/публичные поля и свойства/namespace —
**PascalCase**; локальные переменные и параметры — **camelCase**; приватные/защищённые/
internal поля и свойства — **\_camelCase**; константы — **CONSTANT_NAME_CASE**.
Соглашение не зависит от `const`/`static`/`readonly`. Интерфейсы — с `I` (`IInterface`).
Асинхронные методы — суффикс `Async`. Имя метода точно отражает его содержание.
Для регистра «слово» — всё без внутренних пробелов, включая аббревиатуры (`MyRpc`, не `MyRPC`).

### Соответствие нотации и элемента языка

| Элемент языка | Нотация | Пример |
|---|---|---|
| Класс, структура | PascalCase | `AppDomain` |
| Интерфейс | PascalCase | `IBusinessService` |
| Перечисление (тип/значение) | PascalCase | `ErrorLevel` / `FatalError` |
| Событие | PascalCase | `Click` |
| Приватное поле | _camelCase | `_listItem` |
| Защищённое поле | PascalCase | `MainPanel` |
| Константное поле | CONSTANT_CASE | `MAXIMUM_ITEMS` |
| Read-only статическое поле | PascalCase | `RedValue` |
| Локальная переменная | camelCase | `listOfValues` |
| Метод / локальная функция | PascalCase | `ToString` / `FormatText` |
| Пространство имён | PascalCase | `System.Drawing` |
| Параметр | camelCase | `typeName` |
| Параметр типа | PascalCase | `TView` |
| Свойство | PascalCase | `BackColor` |
| Кортеж | camelCase | `firstName` |

Дополнительно:

- Имена — из американского английского; читаемость важнее краткости; избегать конфликтов с ключевыми словами.
- Типы атрибутов заканчиваются на `Attribute`; перечисления — единственное число (нефлаги) / множественное (флаги).
- Идентификаторы без двух подряд `__`. Приватные поля — с `_` + camelCase.
- Для `private`/`internal` static-полей — префикс `s_`, для статических потоковых — `t_`.
- Поля в JSON, принимаемых/возвращаемых API, — **camelCase**.

## 5. Структура класса

Порядок членов класса:

1. Вложенные классы, перечисления, делегаты, события.
2. Статические, константные и read-only поля.
3. Конструкторы и финализаторы.
4. Свойства.
5. Методы.

Внутри каждой группы — по доступности: `public → internal → protected internal → protected → private`.
Реализации интерфейсов по возможности группировать вместе. Сводный порядок:

```
static, const
private readonly
private constructor
public constructor
public свойство
private свойство
public method
private method
static method
```

## 6. Оформление DTO

- DTO, используемые на frontend, помечаются `[TsInterface]` (кодогенерация TypeScript через ReinforcedTypings).
- Для каждого метода API — отдельные `Request` и `Response` DTO.

## 7. Руководство по кодированию C#

- Неиспользуемый и закомментированный код не попадает в PR / общую кодовую базу.
- **Константы:** что можно — делать `const`, иначе `readonly`; без «магических» констант — только именованные.
- **Коллекции:** на входе — максимально ограничивающий тип (`IReadOnlyCollection`/`IReadOnlyList`/`IEnumerable`), если данные неизменяемы; на выходе — `IList`, если передаётся владение, иначе наиболее ограничивающий.
- **Генераторы против контейнеров:** по здравому смыслу (читаемость vs производительность; ленивость; повторный обход).
- **Свойства:** read-only в одну строку — через тело выражения (`int SomeProperty => _someProperty`); остальное — `{ get; set; }`.
- **Лямбды против методов:** нетривиальная или переиспользуемая лямбда → именованный метод.
- **Методы расширения:** только если исходный код недоступен/неизменяем и функциональность «основная»; в core-библиотеки — только повсеместно доступные; минимизировать использование.
- **`ref`/`out`:** `out` — для возвратов, не являющихся входами, и после остальных параметров; `ref` — редко, только когда нужно заменить экземпляр контейнера; не для оптимизации передачи структур.
- **LINQ:** каждый метод цепочки — с новой строки с точки (искл. одиночный метод); аргументы предикатов именовать по сущности (`pos => pos.Id`, допускается первая буква); методы выборки из БД возвращают `IQueryable`, материализация — на уровне services, не выше контроллера; предпочитать короткие однострочные LINQ и императивный код длинным цепочкам; member-методы вместо SQL-стиля; избегать `ForEach(...)` длиннее одного выражения.
- **Array vs List:** в общем случае `List<>` для публичных переменных/свойств/возвратов; массивы — когда размер фиксирован/известен; для многомерных — массив.
- **Кортежи:** для сложных возвратов — именованный тип, а не `Tuple<>`.
- **Строки:** интерполяция на основе выражений для коротких строк; в циклах/больших текстах — `StringBuilder`; предпочитать raw string literals.
- **`var`:** когда тип очевиден (`var apple = new Apple()`) или для временных переменных, передаваемых дальше; не использовать для базовых/числовых типов и когда тип важен пользователю.
- **Атрибуты:** на отдельной строке над членом, отделены пустой строкой; несколько — каждый с новой строки.

## 8. Документирование кода

- Описывается назначение каждого класса и всех методов (включая `private`).
- Публичные элементы — XML-комментарии (`///`) с элементами `<param>`, `<returns>`, `<remarks>`, `<exception>` (см. [xmldoc](https://learn.microsoft.com/ru-ru/dotnet/csharp/language-reference/xmldoc/)).
- Краткие пояснения — однострочный `//` на отдельной строке (не в конце строки кода), с заглавной буквы и точкой в конце.
- `/// <inheritdoc />` при документировании реализации **не** используется.

## 9. Типовая структура сервиса

Чистая архитектура; слои (больший номер зависит от меньшего; слой 0/1 ни от чего не зависит):

| Папка | Проект | Описание |
|---|---|---|
| 0 Utils | `Ritm.[ServiceName].Utils` | Общая функциональность (логирование и т.п.) |
| 1 Entities | `Ritm.[ServiceName].Entities` | Только Entities (Rich-модель), без интерфейсов репозитория |
| 1 Entities | `Ritm.[ServiceName].DomainInterfaces` | Интерфейсы доменных сервисов |
| 1 Entities | `Ritm.[ServiceName].DomainServices` | Реализация доменной логики |
| 2 Infrastructure.Interfaces | `Ritm.[ServiceName].Dal.Interface` | Ссылка на EF Core |
| 2 Infrastructure.Interfaces | `Ritm.[ServiceName].Kafka.Interface` | Доступ к шине данных |
| 3.1 ApplicationServices | `Ritm.[ServiceName].AppServices` / `.AppInterfaces` | Общая логика модуля (операции для нескольких handlers) |
| 3.2 UseCases | `Ritm.[ServiceName].UseCases` | Пользовательские сценарии, CQRS, MediatR |
| 4 Controllers | `Ritm.[ServiceName].Controllers` | Controllers, Middleware, Filters (API) |
| 5 Infrastructure.Implementation | `Ritm.[ServiceName].Dal.PgSql` | Доступ к данным (Npgsql.EntityFrameworkCore.PostgreSQL) |
| 5 Infrastructure.Implementation | `Ritm.[ServiceName].Kafka.Implementation` | Реализация интеграции с шиной |
| 6 WebApp | `Ritm.[AppName].WebApp` | Разворачиваемое веб-приложение (MediatR) |
| 7 Plugins | `Ritm.[ServiceName].Plugins` | Регистрация сервисов модуля |
| 8 Tests | `Ritm.[ServiceName].Tests`, `...UseCases.Tests.Unit` | Тесты |

**Наименование проектов:** `[Организация].[Сервис].[Функциональное назначение]`
(напр. `Ritm.Portal.WebApp`; на проекте РИТМ организация всегда `Ritm`).
Интеграционные: `[Организация].[Сервис].Integration.[Назначение]`.

**Положения:**
- Монолит: реализуются уровни 1–5 и 7 в папке `Modules`; модуль подключается к единому веб-приложению через Plugins.
- Сервис (микросервис): реализуются все уровни, кроме 7, в папке веб-приложения; общее для нескольких микросервисов выносится в `Modules`.
- Интеграционная часть — в папке модуля по чистой архитектуре.

## 10. Типовая структура UseCases

CQRS-раскладка (на примере `EuroChem.ServiceName.UseCases`):

```
Handlers/
  Orders/
    Commands/
      CreateOrder/
        Validators/CreateOrderValidator.cs
        Requests/CreateOrderRequest.cs
        Responses/CreateOrderResponse.cs
        Dto/ProductDto.cs
        CreateOrderCommand.cs
        CreateOrderCommandHandler.cs
    Queries/
      GetOrders/
        Validators/GetOrderValidator.cs
        Requests/GetOrderRequest.cs
        Responses/GetOrderResponse.cs
        Dto/OrderDto.cs, ProductDto.cs
        GetOrdersQuery.cs
        GetOrdersHandler.cs
    Mappings/ProductMappings.cs
    Enums/OrderBy.cs, OrderDirection.cs
```

## 11. Разделение разработки по инсталляциям (ЕХ–СГК)

Для отдельной инсталляции РИТМ под СГК (ЦОД M1) процесс разработки разделён:

- Общие модули — в отдельный git-репозиторий, на их базе — NuGet-пакеты.
- Core-сервисы — в отдельный git-репозиторий.
- Core-пакеты и сервисы переиспользуются и на ЕХ, и на СГК.
- Бизнес-модули разделяются в разные кодовые базы и развиваются параллельно.
- В Bamboo — разные deploy для сборки ЕХ и СГК.

(Схема подхода — drawio-диаграмма «Подход_к_разработке_ЕХ_СГК» на исходной странице.)
