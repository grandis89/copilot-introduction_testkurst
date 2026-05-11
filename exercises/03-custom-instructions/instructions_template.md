# Custom Instructions Template

> Copy this file to `.github/copilot-instructions.md` and customise it for your project.
> Delete sections that don't apply. Add your own rules.

---

## Project Context

<!-- Describe what this project does in 2-3 sentences -->
This project is a [describe your project here]. It [what it processes/produces] for [who uses it].

## Language & Runtime

- Python [version, e.g. 3.11]
- Key libraries: [list the ones you actually use]

## Coding Style

- Use type hints on all function signatures
- Write docstrings for every public function (Google style)
- Prefer [f-strings / .format() / % — pick one]
- Use the `logging` module; do not use `print()` for anything other than user-facing output

## Naming Conventions

- Variables and functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- [Add any project-specific naming rules here]

## What NOT to Do

- Do not suggest [library or pattern you want to avoid]
- Do not use hardcoded file paths — always use `pathlib.Path`
- [Add other anti-patterns specific to your project]

## SQL Conventions

- SQL dialect: [e.g., T-SQL for Fabric Warehouse, PostgreSQL, ANSI]
- Always alias tables with meaningful short names (e.g., `orders AS o`)
- Prefer CTEs over nested subqueries for readability

## Testing

- Framework: pytest
- Test file naming: `test_<module>.py`
- [Any other testing conventions]
