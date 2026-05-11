# Exercise 04 — GitHub.com Features

**Time:** ~10 minutes  
**Goal:** Use GitHub Copilot features that live on GitHub.com — PR descriptions and Copilot on issues.

---

## Background

Copilot isn't only in your editor. On GitHub.com, Copilot can:
- Generate pull request descriptions from your diff
- Help you understand and respond to issues

This exercise walks you through a small bug fix, getting it to GitHub, and letting Copilot handle the PR write-up.

---

## Steps

### 1. Fix the bug

Open `bugfix.py` in VS Code. The file contains a function with a real bug.

Read the code and try to spot the bug yourself first — then ask Copilot Chat:

> "Does this function have any bugs? Explain what they are."

Fix the bug (with or without Copilot's help).

### 2. Stage and commit

Open the integrated terminal (`Ctrl+` `` ` ``) and run:

```bash
git add exercises/04-github-features/bugfix.py
git commit -m "fix: correct revenue calculation in calculate_discount"
```

### 3. Push to your fork

```bash
git push origin master
```

### 4. Open a Pull Request on GitHub

1. Go to your fork on GitHub.com
2. Click **"Compare & pull request"** (the yellow banner) or go to **Pull requests → New pull request**
3. Set the base repository to **your own fork** (not the original repo), base branch `master`

### 5. Use Copilot to generate the PR description

In the PR creation form, look for the **Copilot icon** (✨) next to the description box.  
Click it → **"Generate with Copilot"**.

Review the generated description. Does it accurately describe the change? Edit it if needed, then submit the PR.

### 6. (Optional) Explore Copilot on an issue

Go to the **Issues** tab on your fork and create a new issue describing a hypothetical problem, e.g.:

> "The summarise_by_category function is slow for large files."

Once created, look for the Copilot button inside the issue — you can ask Copilot to suggest a solution or summarise the issue.

---

## What to Try

- After the PR is created, go to the **Files changed** tab. Hover over a line — does Copilot offer suggestions?
- Ask Copilot in the issue: *"What are some ways to optimise this for large files?"*

---

## Tip

Copilot's PR description quality depends on how atomic your commits are. A commit that does one clear thing produces a much better description than a commit that changes 10 unrelated things.

---

## Done?

Move on to **Exercise 05 →**
