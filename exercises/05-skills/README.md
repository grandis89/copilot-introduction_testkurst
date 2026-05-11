# Exercise 05 — Skills & Slash Commands

**Time:** ~10 minutes  
**Goal:** Master the built-in Copilot Chat slash commands and the `@workspace` participant.

---

## Background

Copilot Chat has a set of built-in **skills** you trigger with slash commands. These are shortcuts for common developer tasks that go beyond "write code for me".

| Command | What it does |
|---------|-------------|
| `/explain` | Explains selected code in plain English |
| `/fix` | Diagnoses and suggests a fix for a problem |
| `/tests` | Generates unit tests for selected code |
| `/doc` | Generates a docstring or documentation comment |
| `@workspace` | Searches across your whole project, not just the open file |

---

## Steps

### 1. Open the messy file

Open `messy_pipeline.py`. It's a real-looking (but fictional) data pipeline with no documentation, inconsistent style, and a couple of bugs.

Read it — or don't. That's the point of `/explain`.

### 2. Use `/explain`

Highlight the entire file content (or just a confusing section). In Copilot Chat, type:

```
/explain
```

Read the explanation. Does Copilot correctly identify what the script does? What about the tricky parts?

Try highlighting just one function and running `/explain` again — notice how context changes the depth of the explanation.

### 3. Use `/fix`

The file has at least one bug. Highlight the suspicious function and type:

```
/fix
```

Review the suggested fix. Ask Copilot to explain *why* the original code was wrong before applying the fix.

### 4. Use `/tests`

Highlight one of the functions in the file. In Copilot Chat, type:

```
/tests
```

Review the generated tests. Are they meaningful? Do they cover edge cases?  
Ask Copilot to add a test for a specific edge case you're worried about.

### 5. Use `@workspace`

In Copilot Chat (with no code highlighted), type:

```
@workspace Where is the sales CSV data loaded in this project?
```

Copilot should search across all files in the repo and point you to the right place. Try other cross-project questions:

```
@workspace What functions deal with revenue calculation?
@workspace Are there any functions without docstrings?
```

---

## What to Try

- Use `/doc` on a function to generate a docstring automatically.
- Ask `@workspace`: *"Summarise what this project does based on all the files."*
- Highlight a confusing variable name and ask: *"Suggest a better name for this variable and explain why."*

---

## Tip

`@workspace` is most powerful in larger projects. In this repo it's small, but imagine using it in a 50-file codebase — being able to ask questions across all files without manually searching is a huge time saver.

---

## Done? 🎉

You've completed all five exercises! If you have time left, head to **exercises/bonus/** for an open-ended Agent Mode challenge.
