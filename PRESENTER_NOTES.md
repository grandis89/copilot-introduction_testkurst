# Presenter Notes — 10-Minute Verbal Introduction

> These are speaker notes for the facilitator. The audience has just completed a Git introduction and has VS Code + Copilot installed.

---

## Slide / Talking Point Flow

### 1. What is GitHub Copilot? (2 min)

> "GitHub Copilot is an AI pair programmer built into your editor. It's trained on a large amount of publicly available code and uses the context of what you're writing to suggest completions — whole lines, whole functions, even entire files."

Key points:
- It is **not** a search engine and **not** a replacement for thinking.
- Think of it as a very fast, always-available colleague who has seen a lot of code.
- It reads your **comments, function names, variable names, and open files** to understand context.
- Works in VS Code, Visual Studio, JetBrains IDEs, and more — today we focus on VS Code.

---

### 2. The Three Main Ways to Use Copilot in VS Code (3 min)

**a) Inline completions**
- Start typing (or write a comment describing what you want), and Copilot suggests the rest.
- Accept with `Tab`, dismiss with `Esc`, cycle suggestions with `Alt+]` / `Alt+[`.

**b) Copilot Chat**
- A conversation panel (`Ctrl+Alt+I`). Ask questions, request refactors, explain code.
- You can highlight code and ask Copilot about just that selection.
- Useful quick actions via right-click → Copilot.

**c) Agent Mode**
- Copilot takes multi-step actions: reads files, runs terminal commands, edits across files.
- Higher autonomy — great for scaffolding a feature from a high-level description.
- We'll touch on this in the bonus exercise.

---

### 3. GitHub.com Features (1 min)

> "Copilot isn't only in your editor — it also lives on GitHub.com."

- **Pull request summaries**: Copilot can draft a PR description from your diff.
- **Copilot on issues**: Ask Copilot questions about an issue's context.
- We'll practise this in Exercise 04.

---

### 4. Custom Instructions (2 min)

> "One of the most powerful things you can do is tell Copilot about your project once, so it always responds in the right way."

- Create a file at `.github/copilot-instructions.md` in your repo.
- Copilot Chat automatically includes it in every conversation in that workspace.
- Use it for: coding style, preferred libraries, domain terminology, what *not* to suggest.

Example:
```markdown
We use Python 3.11 and pandas. Always use type hints. Never suggest `print` for logging — use the `logging` module instead.
```

We'll set this up in Exercise 03.

---

### 5. Skills & Slash Commands (1 min)

> "Copilot Chat has built-in skills you trigger with slash commands."

| Command | What it does |
|---------|-------------|
| `/explain` | Explains selected code in plain language |
| `/fix` | Suggests a fix for a bug or error |
| `/tests` | Generates unit tests for selected code |
| `/doc` | Generates documentation/docstrings |

`@workspace` — prefix a question with this to make Copilot search across your entire project, not just the open file.

We'll practise these in Exercise 05.

---

### 6. What's Next: MCP Servers (30 sec)

> "Today we stop at skills. In the next session, we'll go one step further: MCP servers, which let Copilot connect to external tools and APIs — databases, ticketing systems, internal documentation. That's where it gets really powerful for day-to-day data work."

---

## Transition to Exercises

> "Let's switch to hands-on mode. Open your VS Code, make sure Copilot is active (you should see the Copilot icon in the status bar), and navigate to Exercise 01 in the repo. I'll be walking around — raise your hand if you get stuck."

- Point participants to `exercises/01-first-contact/README.md` to start.
- Remind them each exercise has a solution file if they get completely stuck.
- Bonus exercise is in `exercises/bonus/` for those who finish early.
