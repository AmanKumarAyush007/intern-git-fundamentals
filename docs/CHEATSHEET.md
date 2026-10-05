# Git Cheat Sheet

## Everyday

| Task | Command |
|------|---------|
| Status | `git status` |
| See changes | `git diff` / `git diff --staged` |
| Stage file / all | `git add <file>` / `git add -A` |
| Commit | `git commit -m "feat: message"` |
| History | `git log --oneline --graph --all` |
| Show a commit | `git show <hash>` |

## Branches

| Task | Command |
|------|---------|
| List | `git branch -a` |
| Create + switch | `git switch -c <name>` |
| Switch | `git switch <name>` |
| Rename current | `git branch -m <new-name>` |
| Delete local | `git branch -d <name>` |
| Delete remote | `git push origin --delete <name>` |

## Remotes

| Task | Command |
|------|---------|
| List | `git remote -v` |
| Add upstream | `git remote add upstream <url>` |
| Download without merging | `git fetch upstream` |
| Fetch + merge | `git pull` |
| Push new branch | `git push -u origin <branch>` |
| Sync fork main | `git switch main && git fetch upstream && git merge upstream/main && git push origin main` |

## Undo (from safest to riskiest)

| Situation | Command |
|-----------|---------|
| Unstage a file | `git restore --staged <file>` |
| Discard local edits in a file | `git restore <file>` (cannot be undone) |
| Fix last commit message | `git commit --amend -m "new"` (before pushing) |
| Undo a pushed commit safely | `git revert <hash>` (creates a new commit) |
| Move branch back, keep changes | `git reset --soft HEAD~1` |
| Move branch back, drop changes | `git reset --hard HEAD~1` (dangerous) |
| Find lost commits | `git reflog` |
| Save work temporarily | `git stash` / `git stash pop` |

## Merging and rebasing

| Task | Command |
|------|---------|
| Merge | `git merge <branch>` |
| Abort merge | `git merge --abort` |
| Rebase onto main | `git rebase main` |
| Interactive rebase | `git rebase -i HEAD~N` |
| Continue / abort rebase | `git rebase --continue` / `git rebase --abort` |
| Safe force push | `git push --force-with-lease` |
| Cherry-pick | `git cherry-pick <hash>` |

## Inspecting

| Task | Command |
|------|---------|
| Who changed this line | `git blame <file>` |
| Search history | `git log -S "text"` |
| Compare branches | `git diff main..feature` |
| Commits only on branch | `git log main..feature --oneline` |

## Vocabulary

| Term | Meaning |
|------|---------|
| HEAD | The commit you are currently on |
| origin | Your remote (your fork) |
| upstream | The original repo you forked from |
| Working tree | Files on disk |
| Staging area (index) | What will go into the next commit |
| Fast-forward | Merge that just moves the pointer, no merge commit |
| Detached HEAD | HEAD points at a commit, not a branch; `git switch -c <name>` to keep work |

## The commit workflow in one picture

```
working tree --git add--> staging area --git commit--> local repo --git push--> remote
```
