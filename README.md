# intern-git-fundamentals

Welcome to the **SCAI engineering internship**. This repository teaches the Git and GitHub workflow we use every day on the real platform. You will learn by doing: every exercise ends with a Pull Request.

> **Time needed:** 1 to 2 days  |  **Level:** beginner  |  **Tools:** Git, a GitHub account, Python 3.9+ (only for the verify script)

## What you will practice

| # | Exercise | Skill | Guide |
|---|----------|-------|-------|
| 0 | Setup | Install Git, configure identity, SSH or HTTPS auth | [docs/00-setup.md](docs/00-setup.md) |
| 1.1 | Basic Git flow | Fork, clone, branch, commit, push, open a PR | [docs/01-basic-git-flow.md](docs/01-basic-git-flow.md) |
| 1.2 | Merge conflicts | Read conflict markers, resolve, merge commit | [docs/02-merge-conflicts.md](docs/02-merge-conflicts.md) |
| 1.3 | Issues and linked PRs | Branch naming, `Closes #N`, issue tracking | [docs/03-issues-and-linked-prs.md](docs/03-issues-and-linked-prs.md) |
| 1.4 | Code review | Inline comments, request changes, approve | [docs/04-code-review.md](docs/04-code-review.md) |
| 1.5 | Rebase and squash | `git rebase -i`, squash, `--force-with-lease` | [docs/05-rebase-and-squash.md](docs/05-rebase-and-squash.md) |

Helpful extras:
- [Git cheat sheet](docs/CHEATSHEET.md)
- [Grading rubric](docs/GRADING.md)
- [Contribution rules](CONTRIBUTING.md)

## How this repo is organized

```
intern-git-fundamentals/
├── README.md                  <- you are here
├── CONTRIBUTING.md            <- commit, branch and PR rules
├── config.json                <- used in Exercise 1.2
├── app/
│   ├── calculator.py          <- has a bug (Issue exercise 1.3)
│   └── text_utils.py          <- missing docstrings (Issue exercise 1.3)
├── docs/                      <- exercise guides, cheat sheet, rubric
│   └── ABOUT.md               <- contains typos (Issue exercise 1.3)
├── exercises/
│   └── 01-basic-flow/         <- put your hello file here (Exercise 1.1)
├── scripts/
│   └── verify.py              <- self-check tool for your work
└── .github/                   <- PR template and automated checks
```

Mentors: see [docs/MENTOR_GUIDE.md](docs/MENTOR_GUIDE.md) for setup instructions.

## Special branches (already in the repo)

| Branch | Used in | Purpose |
|--------|---------|---------|
| `conflict-branch-a` | 1.2 | Changes `config.json` one way |
| `conflict-branch-b` | 1.2 | Changes the same lines another way |
| `messy-commits` | 1.5 | Five sloppy commits to clean up |
| `review/add-discount-helper` | 1.4 | A PR with deliberate mistakes (mentor opens it) |

> **Important when forking:** on the GitHub fork screen, **untick "Copy the `main` branch only"**. Otherwise the special branches will not be in your fork.

## Quick start

```bash
# 1. Fork on GitHub (untick "Copy the main branch only"), then:
git clone git@github.com:<your-username>/intern-git-fundamentals.git
cd intern-git-fundamentals

# 2. Add the original repo as "upstream" so you can pull new changes
git remote add upstream git@github.com:<org>/intern-git-fundamentals.git
git remote -v

# 3. Start with Exercise 1.1
```

Check your work at any time:

```bash
python scripts/verify.py 1.1 --username <your-github-username>
```

## Golden rules

1. **Never push directly to `main`.** Always use a branch and a PR.
2. **One exercise = one branch = one PR.**
3. **Write meaningful commit messages.** `fix` is not a message.
4. **Ask early.** A stuck hour is fine. A stuck day is not.
5. **Pair programming is fine. Copying is not.** Each intern submits their own PRs.
