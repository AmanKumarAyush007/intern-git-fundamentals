# Exercise 0: Setup

Do this once before anything else. **Time: 20 to 30 minutes.**

## 1. Install Git

| OS | How |
|----|-----|
| Windows | Download from https://git-scm.com/download/win (keep defaults; it includes Git Bash) |
| macOS | `brew install git` or install Xcode Command Line Tools |
| Linux | `sudo apt install git` |

Verify:

```bash
git --version      # should print 2.30 or newer
```

## 2. Tell Git who you are

Use the **same email as your GitHub account**, otherwise your commits will not be linked to your profile.

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global pull.rebase false
git config --global core.editor "code --wait"   # optional: VS Code as editor
git config --list --show-origin                 # check it
```

## 3. Authenticate with GitHub

Pick **one**.

### Option A: SSH (recommended)

```bash
ssh-keygen -t ed25519 -C "you@example.com"      # press Enter for defaults
cat ~/.ssh/id_ed25519.pub                       # copy the output
```

GitHub > Settings > SSH and GPG keys > New SSH key > paste. Test:

```bash
ssh -T git@github.com    # "Hi <username>! You've successfully authenticated"
```

### Option B: HTTPS with a token

GitHub > Settings > Developer settings > Personal access tokens > generate with `repo` scope. Use it as the password when Git asks. Git Credential Manager (bundled on Windows/macOS) remembers it.

## 4. Install Python (for the verify script)

Python 3.9 or newer from https://python.org. Check: `python --version`.

## 5. Optional but useful

- **GitHub CLI** (`gh`): https://cli.github.com, then `gh auth login`.
- **VS Code** with the *GitLens* extension for visualising history.

## 6. Learn these 6 words first

| Word | Meaning |
|------|---------|
| Repository (repo) | A project folder tracked by Git |
| Commit | A saved snapshot with a message |
| Branch | A movable pointer to a line of commits |
| Remote | A copy of the repo on a server (`origin`, `upstream`) |
| Fork | Your personal copy of someone else's repo on GitHub |
| Pull Request (PR) | A request to merge your branch into another |

## Checklist

- [ ] `git --version` works
- [ ] `git config user.name` and `user.email` are set
- [ ] SSH or HTTPS auth works
- [ ] `python --version` works
- [ ] You have a GitHub account and can see the course repo

Next: [Exercise 1.1](01-basic-git-flow.md).
