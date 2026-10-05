# Mentor Guide

Everything you need to publish this repo and run the cohort. Interns do not need this file.

## 1. Publish the repository

The local folder is already a Git repo with all special branches created.

```powershell
cd d:\swarelic\intern-git-fundamentals
git branch -a                      # confirm main + 4 exercise branches
```

Create an **empty** repo on GitHub named `intern-git-fundamentals` (no README, no .gitignore), then:

```powershell
git remote add origin git@github.com:<org>/intern-git-fundamentals.git
git push -u origin main
git push origin conflict-branch-a conflict-branch-b messy-commits review/add-discount-helper
```

## 2. Repository settings

| Setting | Value | Why |
|---------|-------|-----|
| Branch protection on `main` | Require PR, require 1 approval, require status check **Checks**, block force pushes | Teaches the real workflow |
| Allow squash/merge commits | Merge commits on, squash on | Both flows are demonstrated |
| Automatically delete head branches | On | Keeps the repo tidy |
| Issues | Enabled | Exercise 1.3 |
| Discussions (optional) | Enabled | Q and A |
| Collaborators | Add interns as **Read** (they fork) | They submit PRs from forks |

> Interns must untick **Copy the main branch only** when forking; this is in the README but remind them on day one.

## 3. Create the three issues (Exercise 1.3)

Create them **in this order** so numbers are #1, #2, #3:

```powershell
gh auth login
.\scripts\create_issues.ps1 -Repo <org>/intern-git-fundamentals
```

Or create them manually using the bodies in [`issues/`](../issues).

## 4. Open the review PR (Exercise 1.4)

```powershell
gh pr create --repo <org>/intern-git-fundamentals --base main --head review/add-discount-helper `
  --title "add stuff" --body "added discount thing, works on my machine"
```

The vague title and body are deliberate. **Do not merge it.**

Planted problems in `app/discount.py`:

| # | Problem |
|---|---------|
| 1 | Unused `import os` and `import sys` |
| 2 | Unused variable `tmp` |
| 3 | Missing docstring |
| 4 | Magic number `0.15` and `100` |
| 5 | Vague names `d`, `p`, `r` |
| 6 | Bare `except:` that swallows errors |
| 7 | Odd 2-space indentation, mixed with 4 elsewhere in the repo |
| 8 | No validation (negative price or rate above 100) |
| 9 | No tests |
| 10 | Vague PR title and description |

After the intern requests changes, push the fixes to `review/add-discount-helper` (or tell them you did) and let them approve.

For a cohort, open **one review PR per intern** by pushing copies of the branch (`review/add-discount-helper-<name>`).

## 5. Answer key

### 1.1
`exercises/01-basic-flow/<username>/hello.py` with `print("Hello, SCAI!")`, one commit.

### 1.2
```json
{
  "app_name": "scai-demo",
  "environment": "staging",
  "debug": true,
  "log_level": "WARNING",
  "version": "1.0.0"
}
```

### 1.3
- Issue 1: fix `conected`, `teh`, `recieve`, `enviroment`, `sucessfully`.
- Issue 2: `return a + b`.
- Issue 3: one-line docstrings on `slugify`, `title_case`, `truncate`.

### 1.5
`git rebase -i HEAD~5`, mark four as `squash`, one clean message. Final tree equals the branch tip.

## 6. Suggested schedule

| Block | Activity |
|-------|----------|
| Day 1 AM | 15-min talk: what is Git, mental model. Setup (00) |
| Day 1 AM | Exercise 1.1 with live demo |
| Day 1 PM | Exercise 1.2 (do a live conflict first) |
| Day 2 AM | Exercise 1.3 and 1.4 (pair up for reviewing) |
| Day 2 PM | Exercise 1.5, retrospective, Q and A |

## 7. Resetting the exercise branches

If you need to rebuild the special branches (for example, after a test run), use:

```powershell
.\scripts\setup_branches.ps1
```

It deletes and recreates the four exercise branches from `main`. Then force-push them:

```powershell
git push --force origin conflict-branch-a conflict-branch-b messy-commits review/add-discount-helper
```

## 8. Common support questions

| Question | Answer |
|----------|--------|
| "My fork has no `conflict-branch-a`" | They forked with main only. Click **Sync fork** won't help; delete the fork and refork, or `git fetch upstream` then `git switch -c conflict-branch-a upstream/conflict-branch-a` |
| "Check failed: PR title" | Title must match `type: description` |
| "PR shows unrelated commits" | Branch was created from stale `main`; sync fork first |
| "I deleted my work" | `git reflog` |
| "Verify script says not a merge commit" | They rebased or used `--squash`; redo with a plain `git merge` |

## 9. Tracking progress

Create a GitHub Project (board) with columns `To do / In progress / In review / Done` and one card per intern per exercise. Or use a simple checklist issue per intern.
