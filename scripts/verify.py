#!/usr/bin/env python3
"""Self-check tool for the intern-git-fundamentals exercises.

Usage:
    python scripts/verify.py 1.1 --username <github-username>
    python scripts/verify.py 1.2
    python scripts/verify.py 1.3
    python scripts/verify.py 1.5

Only needs Python 3.9+ and Git. Reads your local repo; changes nothing.
"""
import argparse
import ast
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONVENTIONAL = re.compile(r"^(feat|fix|docs|chore|refactor|test|merge)(\(.+\))?: .+")
BAD_WORDS = ["conected", "teh", "recieve", "enviroment", "sucessfully"]

results = []


def git(*args):
    out = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return out.stdout.strip()


def check(ok, label, hint=""):
    results.append(ok)
    print(("  [PASS] " if ok else "  [FAIL] ") + label)
    if not ok and hint:
        print("         hint: " + hint)


def finish():
    print()
    if all(results):
        print("All checks passed. Open your PR!")
        return 0
    print("Some checks failed. Fix them and run this script again.")
    return 1


def verify_1_1(username):
    print("Exercise 1.1: Basic Git flow")
    branch = git("rev-parse", "--abbrev-ref", "HEAD")
    check(
        re.fullmatch(r"feature/.+-hello-world", branch) is not None,
        f"branch name is 'feature/<name>-hello-world' (yours: {branch})",
        "create it with: git switch -c feature/<your-name>-hello-world",
    )
    if not username:
        check(False, "--username was provided", "run: python scripts/verify.py 1.1 --username <github-username>")
        return
    folder = ROOT / "exercises" / "01-basic-flow" / username
    files = [p for p in (folder / "hello.py", folder / "hello.html") if p.exists()]
    check(bool(files), f"exercises/01-basic-flow/{username}/hello.py (or .html) exists")
    if files:
        check("Hello, SCAI!" in files[0].read_text(encoding="utf-8"), "file contains 'Hello, SCAI!'")
    msg = git("log", "-1", "--pretty=%s")
    check(
        re.match(r"^feat: add hello world for .+", msg) is not None,
        f"latest commit message matches 'feat: add hello world for <name>' (yours: {msg!r})",
        'fix with: git commit --amend -m "feat: add hello world for <name>"',
    )
    base = "origin/main" if git("rev-parse", "--verify", "origin/main") else "main"
    count = git("rev-list", "--count", f"{base}..HEAD")
    check(count == "1", f"exactly one commit ahead of {base} (yours: {count})")
    status = git("status", "--porcelain")
    check(status == "", "working tree is clean (everything committed)")


def verify_1_2():
    print("Exercise 1.2: Merge conflicts")
    text = (ROOT / "config.json").read_text(encoding="utf-8")
    check(not re.search(r"^(<<<<<<<|=======|>>>>>>>)", text, re.M), "no conflict markers left in config.json")
    try:
        data = json.loads(text)
        check(True, "config.json is valid JSON")
    except ValueError as exc:
        check(False, "config.json is valid JSON", str(exc))
        return
    check(data.get("environment") == "staging", 'environment is "staging"')
    check(data.get("debug") is True, '"debug": true was kept (from branch A)')
    check(data.get("log_level") == "WARNING", '"log_level": "WARNING" was kept (from branch B)')
    parents = git("rev-list", "--parents", "-n", "1", "HEAD").split()
    check(len(parents) == 3, "HEAD is a merge commit with two parents", "finish the merge with: git commit")


def _load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def verify_1_3():
    print("Exercise 1.3: Issues (reports status of all three)")
    start = len(results)
    about = (ROOT / "docs" / "ABOUT.md").read_text(encoding="utf-8").lower()
    left = [w for w in BAD_WORDS if re.search(rf"\b{w}\b", about)]
    check(not left, "Issue 1: typos fixed in docs/ABOUT.md", f"still misspelled: {', '.join(left)}")
    try:
        calc = _load(ROOT / "app" / "calculator.py")
        check(calc.add(2, 3) == 5, "Issue 2: add(2, 3) == 5", "add() should return a + b")
    except Exception as exc:  # noqa: BLE001
        check(False, "Issue 2: calculator imports", str(exc))
    tree = ast.parse((ROOT / "app" / "text_utils.py").read_text(encoding="utf-8"))
    missing = [
        n.name for n in tree.body
        if isinstance(n, ast.FunctionDef) and not n.name.startswith("_") and not ast.get_docstring(n)
    ]
    check(not missing, "Issue 3: all public functions have docstrings", f"missing: {', '.join(missing)}")
    branch = git("rev-parse", "--abbrev-ref", "HEAD")
    print(f"\n  info: current branch is '{branch}'. Branch should be fix/issue-<N>-<description>")
    print("  info: it is normal for the other two issues to show FAIL; fix only the one you picked.")
    # Passing 1.3 only requires that the issue you picked is fixed.
    results[start:] = [any(results[start:])]


def verify_1_5():
    print("Exercise 1.5: Rebase and squash")
    base = "origin/main" if git("rev-parse", "--verify", "origin/main") else "main"
    count = git("rev-list", "--count", f"{base}..HEAD")
    check(count == "1", f"exactly one commit ahead of {base} (yours: {count})", "git rebase -i HEAD~5, then squash")
    msg = git("log", "-1", "--pretty=%s")
    check(CONVENTIONAL.match(msg) is not None, f"commit message is conventional (yours: {msg!r})")
    check(msg.lower() not in {"fix", "fix2", "wip", "finally fixed"}, "commit message is descriptive")
    check((ROOT / "app" / "feature_flags.py").exists(), "app/feature_flags.py is present")
    body = git("log", "-1", "--pretty=%b")
    check(len(body.strip()) > 0, "commit has an explanatory body (recommended)")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("exercise", choices=["1.1", "1.2", "1.3", "1.5"])
    parser.add_argument("--username", help="your GitHub username (needed for 1.1)")
    args = parser.parse_args()
    {"1.1": lambda: verify_1_1(args.username), "1.2": verify_1_2, "1.3": verify_1_3, "1.5": verify_1_5}[args.exercise]()
    return finish()


if __name__ == "__main__":
    sys.exit(main())
