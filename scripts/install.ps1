# Installs skills from src/ into ~/.claude/skills/ (overwrites same-named).
#
# A directory is a skill only if it contains SKILL.md directly, so reference
# material such as src/references/ is never installed.
#
# Usage:
#   .\install.ps1 [-Dest <path>]           install (default ~/.claude/skills)
#   .\install.ps1 -Check [-Dest <path>]    compare only, write nothing;
#                                          exit 1 if any ai_tools skill differs
#                                          or is missing. Directories in Dest
#                                          that do not come from src are listed
#                                          as "foreign" and are not a failure.
#   Add -Only name1,name2 to install/check an exact subset.
param(
    [string]$Dest = (Join-Path $env:USERPROFILE ".claude\skills"),
    [switch]$Check,
    # Optional exact skill names. Omit to keep the existing install-all behavior.
    [string[]]$Only
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot

# Collect skill directories: src\<group>\<skill>\ that hold a SKILL.md.
$skills = @(Get-ChildItem -Directory -Path (Join-Path $root "src\*\*") |
    Where-Object { Test-Path (Join-Path $_.FullName "SKILL.md") } |
    Sort-Object Name)

$allSkillNames = @($skills.Name)
if ($Only) {
    $unknown = @($Only | Where-Object { $_ -notin $skills.Name })
    if ($unknown.Count) { throw "Unknown skill(s): $($unknown -join ', ')" }
    $skills = @($skills | Where-Object { $_.Name -in $Only })
}

$duplicates = @($skills | Group-Object Name | Where-Object Count -gt 1)
if ($duplicates.Count) { throw "Duplicate skill names: $($duplicates.Name -join ', ')" }

if ($skills.Count -eq 0) {
    Write-Host "no skills found under $root\src (expected src\<group>\<skill>\SKILL.md)"
    exit 1
}

function Get-RelativeFileMap {
    param([string]$Path)
    $map = @{}
    $prefix = (Resolve-Path $Path).Path.TrimEnd('\') + '\'
    Get-ChildItem -Recurse -File -Path $Path | ForEach-Object {
        $rel = $_.FullName.Substring($prefix.Length)
        # Normalize line endings so CRLF/LF checkouts compare equal.
        $text = [System.IO.File]::ReadAllText($_.FullName) -replace "`r`n", "`n"
        $map[$rel] = $text
    }
    return $map
}

if (-not $Check) {
    New-Item -ItemType Directory -Force $Dest | Out-Null
    $resolvedDest = (Resolve-Path -LiteralPath $Dest).Path.TrimEnd('\', '/')
    foreach ($skill in $skills) {
        $target = [System.IO.Path]::GetFullPath((Join-Path $resolvedDest $skill.Name))
        if (-not $target.StartsWith($resolvedDest + [System.IO.Path]::DirectorySeparatorChar, [System.StringComparison]::OrdinalIgnoreCase)) {
            throw "Skill destination escapes install directory: $target"
        }
        if (Test-Path -LiteralPath $target) {
            if ((Get-Item -LiteralPath $target).Attributes -band [System.IO.FileAttributes]::ReparsePoint) {
                throw "Refusing to overwrite linked skill directory: $target"
            }
            Remove-Item -LiteralPath $target -Recurse -Force
        }
        Copy-Item -Recurse $skill.FullName $target
        Write-Host "installed: $($skill.Name) -> $target"
    }
    Write-Host "total: $($skills.Count) skill(s) installed into $Dest"
    exit 0
}

# -Check: report differences, never write anything.
if (-not (Test-Path $Dest)) {
    Write-Host "missing destination: $Dest"
    Write-Host "check FAILED: destination does not exist"
    exit 1
}

$problems = 0
foreach ($skill in $skills) {
    $target = Join-Path $Dest $skill.Name
    if (-not (Test-Path $target)) {
        Write-Host "MISSING:  $($skill.Name) (not installed in $Dest)"
        $problems++
        continue
    }
    $srcMap = Get-RelativeFileMap $skill.FullName
    $dstMap = Get-RelativeFileMap $target
    $bad = @()
    foreach ($rel in $srcMap.Keys) {
        if (-not $dstMap.ContainsKey($rel)) { $bad += "only in src: $rel" }
        elseif ($srcMap[$rel] -ne $dstMap[$rel]) { $bad += "content differs: $rel" }
    }
    foreach ($rel in $dstMap.Keys) {
        if (-not $srcMap.ContainsKey($rel)) { $bad += "only in dest: $rel" }
    }
    if ($bad.Count -gt 0) {
        Write-Host "DIFFERS:  $($skill.Name)"
        $bad | Sort-Object | ForEach-Object { Write-Host "            $_" }
        $problems++
    }
    else {
        Write-Host "ok:       $($skill.Name)"
    }
}

# Extra directories in Dest are reported, but are not a failure.
Get-ChildItem -Directory -Path $Dest | Where-Object { $allSkillNames -notcontains $_.Name } |
    ForEach-Object { Write-Host "foreign:  $($_.Name) (not from ai_tools)" }

if ($problems -gt 0) {
    Write-Host "check FAILED: $problems of $($skills.Count) ai_tools skill(s) differ from src"
    exit 1
}
Write-Host "check OK: all $($skills.Count) ai_tools skill(s) match src"
exit 0
