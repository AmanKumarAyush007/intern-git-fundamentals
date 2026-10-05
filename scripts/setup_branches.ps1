<#
.SYNOPSIS
  (Mentor) Rebuilds the four exercise branches from `main`:
  conflict-branch-a, conflict-branch-b, messy-commits, review/add-discount-helper.
  Safe to re-run: existing exercise branches are deleted and recreated.
.EXAMPLE
  .\scripts\setup_branches.ps1
#>
$ErrorActionPreference = "Stop"
Set-Location (Split-Path -Parent $PSScriptRoot)

if (-not (git config user.name)) { git config user.name "SCAI Mentor" }
if (-not (git config user.email)) { git config user.email "mentor@scai.example" }

if (git status --porcelain) { throw "Working tree not clean. Commit or stash first." }
git switch main | Out-Null

function Reset-Branch($name) {
  if (git branch --list $name) { git branch -D $name | Out-Null }
  git switch -c $name main | Out-Null
}

function Write-Utf8($path, $text) {
  $dir = Split-Path $path
  if ($dir -and -not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }
  [System.IO.File]::WriteAllText((Join-Path (Get-Location) $path), $text.Replace("`r`n", "`n"), (New-Object System.Text.UTF8Encoding $false))
}

# ---------- Exercise 1.2: conflict branches ----------
Reset-Branch "conflict-branch-a"
Write-Utf8 "config.json" @'
{
  "app_name": "scai-demo",
  "environment": "staging",
  "debug": true,
  "version": "1.0.0"
}
'@
git add config.json
git commit -q -m "config: switch environment to staging and enable debug"

Reset-Branch "conflict-branch-b"
Write-Utf8 "config.json" @'
{
  "app_name": "scai-demo",
  "environment": "production",
  "log_level": "WARNING",
  "version": "1.0.0"
}
'@
git add config.json
git commit -q -m "config: switch environment to production and reduce logging"

# ---------- Exercise 1.5: messy commits ----------
Reset-Branch "messy-commits"
$v1 = @'
FLAGS = {"new_dashbord": False}


def is_enabled(name):
    return FLAGS[name]
'@
Write-Utf8 "app/feature_flags.py" $v1
git add app/feature_flags.py
git commit -q -m "fix"

$v2 = @'
FLAGS = {"new_dashbord": False}


def is_enabled(name):
    return FLAGS.get(name)
'@
Write-Utf8 "app/feature_flags.py" $v2
git commit -q -am "fix2"

$v3 = @'
FLAGS = {"new_dashbord": False, "beta_calls": True}


def is_enabled(name):
    return FLAGS.get(name, False)
'@
Write-Utf8 "app/feature_flags.py" $v3
git commit -q -am "finally fixed"

$v4 = @'
FLAGS = {"new_dashboard": False, "beta_calls": True}


def is_enabled(name):
    return FLAGS.get(name, False)
'@
Write-Utf8 "app/feature_flags.py" $v4
git commit -q -am "removed typo"

$v5 = @'
"""Tiny feature flag helper."""

FLAGS = {"new_dashboard": False, "beta_calls": True}


def is_enabled(name):
    """Return True if the named feature flag is on. Unknown flags are off."""
    return FLAGS.get(name, False)
'@
Write-Utf8 "app/feature_flags.py" $v5
git commit -q -am "wip"

# ---------- Exercise 1.4: review branch ----------
Reset-Branch "review/add-discount-helper"
$disc = @'
import os
import sys

def apply_discount(p, r):
  tmp = []
  try:
    d = p * (r / 100)
    if r > 0.15 * 100:
      d = p * 0.15
    return p - d
  except:
    return 0
'@
Write-Utf8 "app/discount.py" $disc
git add app/discount.py
git commit -q -m "add stuff"

git switch main | Out-Null
Write-Host "Branches ready:"
git branch -vv
