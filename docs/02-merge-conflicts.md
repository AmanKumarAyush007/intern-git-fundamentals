# Exercise 1.2: Merge Conflicts

**Goal:** read conflict markers, resolve a conflict by hand, and complete a merge commit.
**Time:** 1 hour.

## The scenario

Two developers changed the same part of `config.json` at the same time:

| Branch | Developer's change |
|--------|--------------------|
| `conflict-branch-a` | `"environment": "staging"` and adds `"debug": true` |
| `conflict-branch-b` | `"environment": "production"` and adds `"log_level": "WARNING"` |

Git cannot decide automatically, so **you** must.

## The decision rule

The release has **not** been approved for production yet. Therefore the final file must:

1. Have `"environment": "staging"`.
2. **Keep** `"debug": true` (from branch A).
3. **Keep** `"log_level": "WARNING"` (from branch B).
4. Stay valid JSON (watch your commas!).

Expected final `config.json`:

```json
{
  "app_name": "scai-demo",
  "environment": "staging",
  "debug": true,
  "log_level": "WARNING",
  "version": "1.0.0"
}
```

## Steps

### 1. Prepare

```bash
git fetch origin
git switch -c fix/merge-config-conflict origin/conflict-branch-a
```

This creates your own working branch starting at branch A.

### 2. Start the merge

```bash
git merge origin/conflict-branch-b
```

Expected output:

```
CONFLICT (content): Merge conflict in config.json
Automatic merge failed; fix conflicts and then commit the result.
```

Do not panic. This is normal.

### 3. See what is going on

```bash
git status          # "both modified: config.json"
git diff            # shows the conflict
```

### 4. Read the conflict markers

Open `config.json`. You will see:

```
<<<<<<< HEAD
  "environment": "staging",
  "debug": true,
=======
  "environment": "production",
  "log_level": "WARNING",
>>>>>>> origin/conflict-branch-b
```

| Marker | Meaning |
|--------|---------|
| `<<<<<<< HEAD` | start of **your current branch's** version (branch A) |
| `=======` | separator |
| `>>>>>>> origin/conflict-branch-b` | end of the **incoming** version (branch B) |

### 5. Resolve

Edit the file by hand so it matches the expected result above. **Delete all three marker lines.** In VS Code you can click *Accept Both Changes* then edit, but always read the result.

Validate:

```bash
python -m json.tool config.json
```

If it prints the JSON back, it is valid.

### 6. Mark resolved and commit

```bash
git add config.json
git status                 # "All conflicts fixed but you are still merging"
git commit                 # accept the default merge message, or:
git commit -m "merge: resolve config.json conflict (staging, keep debug and log_level)"
```

### 7. Check the history

```bash
git log --oneline --graph --all -10
```

You should see a merge commit with **two parents**.

### 8. Verify, push, PR

```bash
python scripts/verify.py 1.2
git push -u origin fix/merge-config-conflict
```

Open a PR to `main` titled `fix: resolve config.json merge conflict`. In the description, explain **why** you chose `staging`.

## Deliverable

A PR whose `config.json` equals the expected file, containing a real merge commit.

## Aborting if you get lost

```bash
git merge --abort      # returns to the state before the merge
```

You can always restart. Nothing is lost.

## Self-check questions

1. Why did Git raise a conflict here but not for different lines?
2. What does `HEAD` mean in the markers?
3. What is the difference between a merge commit and a fast-forward?
4. How could the team avoid this conflict in real life? (Hint: communication, smaller branches, frequent pulls.)

## Common mistakes

| Mistake | Result |
|---------|--------|
| Leaving `<<<<<<<` in the file | Broken JSON and CI fails |
| Missing comma between lines | Invalid JSON |
| Choosing `production` | Fails the rule |
| Running `git add .` without reading the file | You may commit unresolved markers |

Next: [Exercise 1.3](03-issues-and-linked-prs.md).
