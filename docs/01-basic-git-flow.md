# Exercise 1.1: Basic Git Flow

**Goal:** complete the full lifecycle once: **Fork > Clone > Branch > Commit > Push > Pull Request.**
**Time:** 45 minutes.

## The picture

```
 upstream (org/intern-git-fundamentals)
        ^   Pull Request
        |
 origin (you/intern-git-fundamentals)   <- your fork on GitHub
        ^   git push
        |
 local clone on your laptop             <- you work here
```

## Steps

### 1. Fork

On GitHub open the course repo and click **Fork**. **Untick "Copy the `main` branch only"** so you also get the exercise branches.

### 2. Clone your fork

```bash
git clone git@github.com:<your-username>/intern-git-fundamentals.git
cd intern-git-fundamentals
git remote add upstream git@github.com:<org>/intern-git-fundamentals.git
git remote -v        # origin = your fork, upstream = course repo
git status           # "On branch main, nothing to commit"
```

### 3. Create a branch

```bash
git switch -c feature/<your-name>-hello-world
```

Example: `feature/asha-hello-world`. (`git checkout -b` does the same on older Git.)

### 4. Add your file

Create a folder named after your **GitHub username** and a file inside it:

```
exercises/01-basic-flow/<your-github-username>/hello.py
```

Contents:

```python
print("Hello, SCAI!")
```

(You may use `hello.html` instead, containing the text `Hello, SCAI!`.)

Run it: `python exercises/01-basic-flow/<your-github-username>/hello.py`

### 5. Stage and inspect

```bash
git status                  # shows the new file as untracked
git add exercises/01-basic-flow/<your-github-username>/hello.py
git status                  # now "Changes to be committed"
git diff --staged           # review exactly what you will commit
```

### 6. Commit

```bash
git commit -m "feat: add hello world for <your-name>"
git log --oneline -3
```

### 7. Push

```bash
git push -u origin feature/<your-name>-hello-world
```

`-u` links your local branch to the remote one so later you can just type `git push`.

### 8. Open the Pull Request

1. Open your fork on GitHub; click **Compare & pull request**.
2. Check: **base repository** is the course repo, **base** is `main`, **compare** is your branch.
3. Title: `feat: add hello world for <your-name>`
4. Fill in the PR template.
5. Click **Create pull request**.

### 9. Verify

```bash
python scripts/verify.py 1.1 --username <your-github-username>
```

Then wait for the automated checks and your mentor's review. If they request changes, commit on the **same branch** and push; the PR updates itself.

## Deliverable

One PR containing exactly **one commit** and **one new file**.

## Self-check questions (answer in the PR description)

1. What is the difference between `origin` and `upstream`?
2. What does `git add` do, and why is it separate from `git commit`?
3. Why did we not commit to `main`?

## Common problems

| Problem | Fix |
|---------|-----|
| `Permission denied (publickey)` | SSH key not added to GitHub; redo [setup](00-setup.md) step 3 |
| `fatal: not a git repository` | You are in the wrong folder; `cd intern-git-fundamentals` |
| Committed to `main` by mistake | `git switch -c feature/<name>-hello-world` then ask a mentor how to reset `main` |
| PR shows many unrelated commits | Your branch was created from an old `main`; ask for help |
| Wrong commit message | Not pushed yet: `git commit --amend -m "new message"` |

## Concepts recap

- A **commit** is a snapshot, not a diff.
- A **branch** is just a label pointing at a commit; branches are cheap.
- `git push` uploads commits; PRs are a GitHub feature, not Git itself.

Next: [Exercise 1.2](02-merge-conflicts.md).
