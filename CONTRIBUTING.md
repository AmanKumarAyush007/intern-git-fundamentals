# Contributing Guide

These are the same conventions used on the SCAI platform repository.

## Branch names

Format: `<type>/<short-kebab-description>`

| Type | When | Example |
|------|------|---------|
| `feature/` | new work | `feature/asha-hello-world` |
| `fix/` | bug or typo fix | `fix/issue-2-calculator-add` |
| `docs/` | docs only | `docs/update-readme` |
| `chore/` | tooling, cleanup | `chore/squash-feature-flags` |

Rules: lowercase, hyphens, no spaces, no personal jokes.

## Commit messages (Conventional Commits)

```
<type>: <what changed, imperative mood, under 72 chars>

<optional body: why, not how>
```

Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`.

| Bad | Good |
|-----|------|
| `fix` | `fix: correct add() to return the sum` |
| `updated stuff` | `docs: fix three typos in ABOUT.md` |
| `final final v2` | `feat: add feature flag helper` |

Tips:
- Imperative mood: "add", not "added" or "adds".
- One logical change per commit.
- Never commit secrets, `.env` files, or large binaries.

## Pull requests

1. **Title** follows the commit format, for example `feat: add hello world for asha`.
2. **Description** uses the PR template (what, why, how tested, checklist).
3. Link issues with `Closes #N` when the PR fully resolves them.
4. Keep PRs small. One exercise per PR.
5. Respond to every review comment, either with a fix or a reply.
6. Do not merge your own PR. A mentor merges after approval.

## Automated checks

Every PR runs [.github/workflows/checks.yml](.github/workflows/checks.yml):
- PR title format
- No leftover conflict markers (`<<<<<<<`, `>>>>>>>`)
- `config.json` is valid JSON
- Python files compile

A red check means fix it before asking for review.

## Force pushing

Only on **your own feature branch** after a rebase, and always with:

```bash
git push --force-with-lease
```

Never force-push to `main`.
