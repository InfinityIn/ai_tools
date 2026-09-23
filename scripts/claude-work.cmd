@echo off
rem =========================================================================
rem Claude Code CLI — корпоративный контур.
rem Запускает claude с отдельным settings.json (корп. gateway + токен),
rem не трогая глобальный ~/.claude/settings.json личного контура.
rem
rem Использование:
rem   claude-work.cmd                  — старт в D:\work
rem   claude-work.cmd D:\work\ritmportal — старт в конкретном проекте
rem =========================================================================
set "CORP_SETTINGS=C:\Users\ncux2\.claude\1archive\settings.json"

if not exist "%CORP_SETTINGS%" (
    echo [claude-work] Не найден %CORP_SETTINGS%
    pause
    exit /b 1
)

if "%~1"=="" (cd /d D:\work) else (cd /d "%~1")

claude --settings "%CORP_SETTINGS%"
