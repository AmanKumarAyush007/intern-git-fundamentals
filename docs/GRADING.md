# Grading Rubric

Each exercise is graded out of 100 using the same four criteria.

| Criterion | Weight | What a full score looks like |
|-----------|--------|------------------------------|
| PR opened with a clear title and description | 20% | Conventional title, template filled, links issue where relevant |
| Work meets the requirements | 40% | `scripts/verify.py` passes and the mentor's checklist below is satisfied |
| Clean, conventional work | 20% | Branch naming, commit messages, small focused diff, no stray files |
| Reflection / meaningful comment | 20% | Self-check questions answered in the PR or an insightful review comment |

## Per-exercise mentor checklist

### 1.1 Basic flow
- [ ] Branch `feature/<name>-hello-world`
- [ ] File at `exercises/01-basic-flow/<username>/hello.py|html` containing `Hello, SCAI!`
- [ ] One commit: `feat: add hello world for <name>`
- [ ] PR targets `main` of upstream

### 1.2 Merge conflicts
- [ ] `config.json` valid JSON, `environment` is `staging`, `debug` and `log_level` kept
- [ ] History contains a merge commit with two parents
- [ ] PR explains why `staging`

### 1.3 Issues and linked PRs
- [ ] Branch `fix/issue-N-...`
- [ ] PR body contains `Closes #N` and issue auto-closed on merge
- [ ] Minimal diff limited to the issue

### 1.4 Code review
- [ ] At least 3 inline comments in a single review
- [ ] Found at least 5 of the planted problems
- [ ] One "Request changes" followed by an "Approve"
- [ ] Tone is constructive and comments explain why

### 1.5 Rebase and squash
- [ ] Exactly one commit ahead of `main`
- [ ] Conventional message with explanatory body
- [ ] Final file contents match `messy-commits`
- [ ] Used `--force-with-lease`, not `--force`

## Overall outcome

| Total average | Result |
|---------------|--------|
| 85 and above | Excellent, move on to the frontend repo |
| 70 to 84 | Good, fix the weak area then continue |
| Below 70 | Repeat the weak exercises with a mentor |

## Red flags (automatic discussion with mentor)

- Pushing directly to `main`
- Force-pushing to a shared branch
- Committing secrets, `.env`, or large generated files
- Copying another intern's PR
