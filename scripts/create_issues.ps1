<#
.SYNOPSIS
  Creates the three exercise issues in a GitHub repo using the GitHub CLI.
.EXAMPLE
  .\scripts\create_issues.ps1 -Repo my-org/intern-git-fundamentals
#>
param(
  [Parameter(Mandatory = $true)][string]$Repo
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot

foreach ($file in Get-ChildItem (Join-Path $root "issues") -Filter "*.md" | Sort-Object Name) {
  $raw = Get-Content $file.FullName -Raw
  if ($raw -notmatch '(?s)^---\r?\n(.*?)\r?\n---\r?\n(.*)$') { throw "Bad front matter in $($file.Name)" }
  $front = $Matches[1]
  $body = $Matches[2]
  $title = ($front -split "\r?\n" | Where-Object { $_ -like "title:*" }) -replace '^title:\s*"?', '' -replace '"?$', ''
  $labels = (($front -split "\r?\n" | Where-Object { $_ -like "labels:*" }) -replace '^labels:\s*', '')
  Write-Host "Creating: $title"
  $args = @("issue", "create", "--repo", $Repo, "--title", $title, "--body", $body)
  foreach ($l in ($labels -split ",\s*")) { if ($l) { $args += @("--label", $l) } }
  & gh @args
}
Write-Host "Done. Issues were created in order, so they should be #1, #2, #3 on a fresh repo."
