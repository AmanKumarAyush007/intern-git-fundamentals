# Exercise 1.5: Rebase and Squash

**Goal:** turn a messy history into one clean, reviewable commit using interactive rebase.
**Time:** 1 hour.

## The scenario

Branch `messy-commits` has five commits on top of `main`:

```
fix
fix2
finally fixed
removed typo
wip
```

They add a small feature-flag helper in `app/feature_flags.py`. Reviewers do not want to read five noisy commits. You will squash them into one.

## Concepts first

- **Rebase** rewrites history by replaying commits onto a new base.
- **Squash** combines several commits into one.
- Rewriting history changes commit hashes, so pushing needs `--force-with-lease`.

> **Golden rule:** only rewrite history on branches that **only you** use. Never on `main`.

## Steps

### 1. Create your working branch

```bash
git fetch origin
git switch -c chore/squash-feature-flags origin/messy-commits
git log --oneline main..HEAD       # list the 5 commits
```

### 2. Start the interactive rebase

```bash
git rebase -i HEAD~5
```

Your editor opens:

```
pick a1b2c3d fix
pick b2c3d4e fix2
pick c3d4e5f finally fixed
pick d4e5f6a removed typo
pick e5f6a7b wip
```

### 3. Mark commits to squash

Keep the **first** as `pick`; change the rest to `squash` (or `s`):

```
pick a1b2c3d fix
squash b2c3d4e fix2
squash c3d4e5f finally fixed
squash d4e5f6a removed typo
squash e5f6a7b wip
```

Save and close.

### 4. Write the new message

A second editor window shows all five messages. Delete everything and write one proper message:

```
feat: add feature flag helper

Add is_enabled() and a default FLAGS table so features can be toggled
without code changes.
```

Save and close. Expected output: `Successfully rebased and updated`.

### 5. Verify

```bash
git log --oneline main..HEAD     # exactly ONE commit
git diff origin/messy-commits    # no output: the code is identical
python scripts/verify.py 1.5
```

### 6. Force-push safely and open a PR

```bash
git push --force-with-lease -u origin chore/squash-feature-flags
```

Open a PR titled `feat: add feature flag helper`.

> Since this is a **new** branch name, the first push does not strictly need force. Practice the flag anyway: repeat the exercise on a branch you have already pushed (for example, run the rebase again after pushing, and push with `--force-with-lease`).

## If something goes wrong

| Situation | Command |
|-----------|---------|
| Want to abandon the rebase | `git rebase --abort` |
| Stuck in a conflict during rebase | fix the file, `git add`, `git rebase --continue` |
| Squashed the wrong thing after finishing | `git reflog` then `git reset --hard HEAD@{N}` |

`git reflog` is your safety net: Git remembers where HEAD was for about 90 days.

## Other useful rebase commands

| Command | Use |
|---------|-----|
| `reword` | change a commit message only |
| `edit` | stop and amend a commit |
| `drop` | delete a commit |
| `fixup` | like squash but discards the message |
| `git commit --fixup <hash>` + `git rebase -i --autosquash` | fast cleanup workflow |
| `git pull --rebase` | update your branch without a merge commit |

## Deliverable

A PR with exactly **one** commit with a conventional message, with the same final code as `messy-commits`.

## Self-check questions

1. Why is rebasing a shared branch dangerous?
2. What is the difference between `--force` and `--force-with-lease`?
3. When would you prefer **merge** over **rebase**?
4. What is the difference between `squash` and `fixup`?

## Congratulations

You now know the full Git workflow used on SCAI: branch, commit, push, PR, review, resolve conflicts, and clean history. Next repository: `intern-frontend-tasks`.
