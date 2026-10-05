# Exercise 1.4: Code Review

**Goal:** learn to review code kindly, precisely, and usefully, using GitHub's review tools.
**Time:** 45 minutes.

## The scenario

The mentor has opened a PR from branch `review/add-discount-helper` titled **"add stuff"**. It adds `app/discount.py`. The code works, but it contains deliberate quality problems. You are the reviewer.

## Steps

### 1. Read the PR description and the diff

PR page > **Files changed**. Read the whole file before commenting.

### 2. Leave at least 3 inline comments

Hover a line, click the blue **+**, write your comment, then choose **Start a review** (not "Add single comment") so your comments are sent together.

Things to look for (not exhaustive; there are at least 8):

- Unused imports or variables
- Missing docstring
- Inconsistent or non-standard indentation
- "Magic numbers" with no name
- Bare `except:` that hides errors
- Vague names (`x`, `d`, `tmp`)
- Missing input validation
- No tests
- Unhelpful PR title/description

### 3. Request changes

At least one comment must be blocking. On **Finish your review** choose **Request changes** and write a short summary.

### 4. Wait for the fixes

The mentor (acting as author) pushes fixes. You get a notification.

### 5. Re-review and approve

Check each of your comments was addressed. Resolve the conversations. Choose **Approve**.

## How to write a good review comment

| Do | Don't |
|----|-------|
| Be specific: "`d` is unclear; consider `discount_rate`" | "bad naming" |
| Explain **why** | Only say what to change |
| Ask questions: "What happens if `price` is negative?" | Assume bad intent |
| Suggest a fix with a `suggestion` block | Rewrite their whole PR |
| Praise good things too | Only criticise |
| Label severity: `nit:` for tiny issues | Treat everything as blocking |

Using GitHub's suggestion feature:

````
```suggestion
def apply_discount(price, rate):
```
````

## Comment prefixes (we use these on the real team)

| Prefix | Meaning |
|--------|---------|
| `blocker:` | must fix before merge |
| `suggestion:` | recommended improvement |
| `nit:` | style preference, optional |
| `question:` | I do not understand; please explain |
| `praise:` | something done well |

## Self-review checklist (use on your own PRs too)

- [ ] Does it do what the title says, and only that?
- [ ] Are names clear?
- [ ] Are errors handled, not hidden?
- [ ] Any dead code, debug prints, or commented-out code?
- [ ] Are there tests?
- [ ] Is the description clear?

## Deliverable

Link to your submitted review showing 3 or more inline comments, one "Request changes", and a final "Approve". Paste the link in your tracking issue or send it to your mentor.

## Self-check questions

1. What is the difference between **Comment**, **Approve**, and **Request changes**?
2. Why start a review instead of posting single comments?
3. How should you respond if you disagree with a reviewer?

Next: [Exercise 1.5](05-rebase-and-squash.md).
