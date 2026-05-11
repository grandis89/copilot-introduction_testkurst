# Copilot Instructions — Example Template

> This is a template for Exercise 03. Copy this file to `.github/copilot-instructions.md`
> (remove the `.example` from the filename) and customise it for your project.

---

## Project Context

This project is a data engineering pipeline for sales reporting. It processes raw transactional data and produces clean datasets for downstream consumption in Power BI dashboards.

## Language & Runtime

- Python 3.11
- Standard library only for this project (no external dependencies unless agreed upon)
- SQL targets a Fabric Warehouse (T-SQL dialect)

## Coding Style

- Always use **type hints** on function signatures
- Prefer **f-strings** over `.format()` or `%` formatting
- Use the `logging` module — never use `print()` for anything other than user-facing CLI output
- Functions should have **docstrings** (Google style)
- Keep functions small and single-purpose

## Data Conventions

- All dates are stored as `datetime.date` objects, never as strings
- Column names use `snake_case`
- Monetary values are in NOK (Norwegian Krone) unless stated otherwise
- Null handling: always be explicit — use `if value is None` not `if not value`

## What to Avoid

- Do not suggest `pandas` unless explicitly asked — we prefer plain Python and SQL for this project
- Do not generate hardcoded file paths — always use `pathlib.Path`
- Do not suggest `os.path` — use `pathlib` instead

## Testing

- Tests use `pytest`
- Test files are named `test_<module>.py`
- Prefer `assert` statements over `unittest` style
