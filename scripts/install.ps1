# Installs every skill from src/ into ~/.claude/skills/ (overwrites same-named).
param([string]$Dest = (Join-Path $env:USERPROFILE ".claude\skills"))

$root = Split-Path -Parent $PSScriptRoot
New-Item -ItemType Directory -Force $Dest | Out-Null

Get-ChildItem -Directory -Path (Join-Path $root "src\*\*") | ForEach-Object {
    $target = Join-Path $Dest $_.Name
    if (Test-Path $target) { Remove-Item -Recurse -Force $target }
    Copy-Item -Recurse $_.FullName $target
    Write-Host "installed: $($_.Name) -> $target"
}
