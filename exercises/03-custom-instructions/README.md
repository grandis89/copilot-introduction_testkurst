# Exercise 03 — Custom Instructions

**Time:** ~10 minutes  
**Goal:** Set up a `.github/copilot-instructions.md` file and observe how it changes Copilot's behaviour.

---

## Background

Custom instructions let you teach Copilot about *your* project — preferred libraries, coding conventions, domain terminology, and what to avoid. Copilot Chat automatically includes this file in every conversation within the workspace.

This is the equivalent of briefing a new colleague on how your team works.

---

## Steps

### 1. Copy the template

A template file is waiting for you at `.github/copilot-instructions.example.md`.

Copy it to `.github/copilot-instructions.md`:

```bash
# In the terminal (Ctrl+` to open it in VS Code)
cp .github/copilot-instructions.example.md .github/copilot-instructions.md
```

On Windows:
```powershell
Copy-Item .github\copilot-instructions.example.md .github\copilot-instructions.md
```

### 2. Read and customise

Open `.github/copilot-instructions.md`. Read through the template and make at least **two changes** that reflect how you'd actually want Copilot to behave:

- Change the preferred libraries (e.g., add `polars` if that's what you use)
- Add a domain-specific term or naming convention
- Change the monetary currency or date format
- Add a rule about error handling or logging

### 3. Test the instructions — before and after

Open Copilot Chat and ask:

> "Write a function that reads a CSV file and returns a list of rows."

Note the response. Now deliberately **violate** one of your instructions — for example, if you said "never use `print`", ask:

> "Write a function that reads a CSV and prints each row."

Does Copilot follow your instructions, push back, or suggest an alternative? Try a few variations.

### 4. Ask Copilot to reflect on its instructions

In Copilot Chat, ask:

> "What coding conventions should I follow in this project?"

Copilot should reflect back what you wrote in your instructions file.

---

## What to Try

- Add an instruction like *"Always add a docstring to every function"* and then ask Copilot to write a function — does it comply?
- Add domain vocabulary: *"A 'pipeline' in this project refers to a Python script that reads from a CSV and writes to a database table."* Then ask: *"How should I structure a pipeline?"*
- Ask Copilot: *"Review my custom instructions and suggest any improvements."*

---

## Tip

Custom instructions work best when they are **specific and actionable**. Vague instructions like "write clean code" have little effect. Concrete rules like "use `pathlib.Path` instead of `os.path`" have clear impact.

---

## Done?

Move on to **Exercise 04 →**
