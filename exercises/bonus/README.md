# Bonus Exercise — Agent Mode Pipeline

**Time:** Open-ended (for fast finishers)  
**Goal:** Use Copilot's **Agent Mode** to scaffold a complete ETL script from a minimal stub.

---

## Background

Agent Mode is a more autonomous version of Copilot Chat. Instead of answering a single question, it can:
- Read multiple files in your project
- Run terminal commands
- Edit across several files
- Iterate until the task is done

This exercise is deliberately open-ended — there is no solution file. The point is to experience Agent Mode and see how far it can take you.

---

## Activating Agent Mode

In Copilot Chat, click the dropdown next to the **Send** button and switch from **"Ask"** to **"Agent"**.

You should see the mode indicator change. Agent Mode may ask for permission before running terminal commands — that's normal, review and approve each step.

---

## Your Task

Open `pipeline_stub.py`. It's a minimal skeleton of an ETL (Extract, Transform, Load) script.

Use Agent Mode to build it out with this prompt (copy and paste it into Agent Mode):

```
Using the stub in exercises/bonus/pipeline_stub.py and the sample data in data/sales_sample.csv,
build out a complete ETL pipeline that:

1. Reads the CSV data
2. Cleans and validates each row (convert types, skip malformed rows, log warnings)
3. Calculates revenue per order (quantity * unit_price)
4. Produces three summary outputs:
   a. Total revenue by region
   b. Top 5 products by revenue
   c. Monthly revenue trend for 2025
5. Writes the summaries to a reports/ folder as separate CSV files
6. Logs progress at each step using the logging module

Use only Python standard library (no pandas). Add type hints and docstrings. 
Follow the instructions in .github/copilot-instructions.md if it exists.
```

---

## What to Observe

- How does Agent Mode break the task into steps?
- Does it read existing files before writing new ones?
- Does it ask for clarification, or does it make decisions on its own?
- How does it handle errors if something goes wrong?

---

## Stretch Goals

If Agent Mode finishes quickly, extend the task:

- *"Add a function that detects and reports any duplicate order_ids in the source CSV."*
- *"Write a pytest test suite for the cleaning and calculation functions."*
- *"Add a command-line argument to filter the output by region."*

---

## Tip

Agent Mode works best with **clear, specific prompts**. If the output isn't what you expected, you don't need to start over — just follow up:

> *"The monthly revenue output is missing months with zero orders. Fix that."*
