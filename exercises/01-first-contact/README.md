# Exercise 01 — First Contact

**Time:** ~10 minutes  
**Goal:** Get comfortable with Copilot's two core features — inline completions and Copilot Chat.

---

## Background

You've been given a partially written Python script (`transform.py`) that loads sales data and cleans it up. Several functions are incomplete — your job is to finish them **using Copilot**, not by writing the code yourself.

---

## Steps

### 1. Open the starter file

Open `exercises/01-first-contact/transform.py` in VS Code.

Read through the file to understand what it does. Notice the `# TODO` comments — those are your targets.

### 2. Use inline completions to complete a function

Go to the `calculate_revenue` function. Place your cursor on the line after the docstring and **start typing** — Copilot will suggest the implementation. Press `Tab` to accept.

> **Tip:** If the suggestion isn't right, press `Esc` and try typing a bit more to give Copilot more context. You can also cycle through alternative suggestions with `Alt+]` (Windows/Linux) or `Option+]` (Mac).

### 3. Write a comment to guide Copilot

Find the `filter_by_region` function. Instead of typing code, write a comment describing what the function should do:

```python
# return only rows where the region matches the given region string
```

Press `Enter` and watch Copilot suggest the implementation.

### 4. Ask Copilot Chat to complete a function

Highlight the entire `summarise_by_category` function (including its docstring and the `pass` statement).

Open Copilot Chat (`Ctrl+Alt+I`) and type:

> "Implement this function so it returns a dictionary mapping each category to its total revenue."

Review the suggestion, then apply it to the file.

### 5. Ask Copilot to explain code

Highlight the `load_csv` function and ask Copilot Chat:

> "Explain what this function does, line by line."

---

## What to Try

Once the TODOs are done, experiment:

- Ask Copilot Chat: *"What happens if the CSV file doesn't exist? How should I handle that?"*
- Ask Copilot to add type hints to any function that's missing them.
- Ask Copilot: *"Write a main() function that loads the CSV, cleans it, and prints the category summary."*

---

## Tip

The **quality of Copilot's suggestions depends on context**. The more descriptive your function names, docstrings, and comments are, the better the suggestions become. Try renaming a variable to something vague and see what happens.

---

## Done?

Check your work against `transform_solution.py`, then move on to **Exercise 02 →**
