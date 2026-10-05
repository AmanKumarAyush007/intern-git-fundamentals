# Exercise 1.3: Issues and Linked Pull Requests

**Goal:** work the way real teams do: from a tracked issue to a PR that closes it automatically.
**Time:** 1 hour.

## Why issues?

An **issue** is a written record of a bug or task. It gives the team one place to discuss, assign, and track work. A PR that says `Closes #N` links to the issue and **closes it automatically when merged**.

## The three open issues

The mentor creates these issues in the upstream repo (bodies live in [`issues/`](../issues)):

| Issue | Title | File |
|-------|-------|------|
| #1 | Fix typos in docs/ABOUT.md | `docs/ABOUT.md` |
| #2 | Bug: `add()` returns the wrong result | `app/calculator.py` |
| #3 | Add docstrings to text_utils functions | `app/text_utils.py` |

> Issue numbers may differ in your copy of the repo. Use the real numbers you see on GitHub.

**Pick any one issue.** If you finish early, do the other two as separate PRs.

## Steps

### 1. Read the issue carefully

Open the issue on GitHub. Reproduce the problem. Comment `I'll take this` so nobody duplicates work.

### 2. Sync your fork

```bash
git switch main
git fetch upstream
git merge upstream/main     # or: git pull upstream main
git push origin main
```

### 3. Create a branch with the issue number

Format: `fix/issue-<number>-<short-description>`

```bash
git switch -c fix/issue-2-calculator-add
```

### 4. Fix the problem

| Issue | What to do |
|-------|-----------|
| Typos | Correct every misspelled word in `docs/ABOUT.md` (there are five) |
| Bug | Make `add(a, b)` return the sum; test with `python -c "from app.calculator import add; print(add(2, 3))"` (expect `5`) |
| Docstrings | Add a one-line docstring to **each** public function in `app/text_utils.py` |

Keep the change **minimal**: fix only what the issue describes.

### 5. Check your fix

```bash
python scripts/verify.py 1.3
```

It reports which of the three issues are currently fixed on your branch.

### 6. Commit

```bash
git add -A
git commit -m "fix: correct add() to return the sum"
```

Include the reason in the commit body if it is not obvious.

### 7. Push and open the PR

```bash
git push -u origin fix/issue-2-calculator-add
```

PR description must include the closing keyword on its own line:

```
Closes #2
```

Accepted keywords: `Closes`, `Fixes`, `Resolves` (case-insensitive).

### 8. Merge

After CI is green and a mentor approves, the mentor merges. Watch the issue close automatically.

## Deliverable

A PR from `fix/issue-N-...` with `Closes #N`, approved and merged, and the linked issue closed.

## Self-check questions

1. What happens to the issue when your PR is merged?
2. Why include the issue number in the branch name?
3. When would you use `Related to #N` instead of `Closes #N`?
4. Why keep the change minimal?

## Writing a good issue (bonus)

Open a new issue of your own using the **Bug report** template. Describe a real or imagined problem with: summary, steps to reproduce, expected result, actual result.

Next: [Exercise 1.4](04-code-review.md).
