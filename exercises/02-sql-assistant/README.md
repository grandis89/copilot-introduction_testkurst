# Exercise 02 — SQL Assistant

**Time:** ~10 minutes  
**Goal:** Use Copilot Chat to write and improve SQL queries against a fictional sales database.

---

## Background

You have a SQL schema (`schema.sql`) representing three tables: `customers`, `products`, and `orders`. Your job is to write queries in `challenges.sql` using **Copilot Chat** — not from memory.

This mirrors real data engineering work: translating business questions into SQL.

---

## Steps

### 1. Open and read the schema

Open `schema.sql` and read through the table definitions. Understanding the schema is step one — Copilot works better when *you* understand the domain too.

### 2. Open the challenges file

Open `challenges.sql`. Each challenge is a commented business question followed by an empty block where you should write the query.

### 3. Use Copilot Chat to write each query

For each challenge:
1. Highlight the comment describing the challenge.
2. Open Copilot Chat and paste or type the business question, for example:

   > "Write a SQL query that shows total revenue per region, ordered from highest to lowest."

3. Review the suggestion, paste it into the file, and adjust if needed.

> **Tip:** Give Copilot the schema context. You can paste the `CREATE TABLE` statements into the chat, or simply say *"using the schema in schema.sql"* — if that file is open, Copilot can reference it.

### 4. Optimise a query

One of the challenges asks you to spot a performance problem in a provided query. Ask Copilot:

> "This query runs slowly on a large table. What would you change to optimise it, and why?"

---

## What to Try

- Ask Copilot to add a `WHERE` clause to filter by date range.
- Ask Copilot: *"Rewrite this query using a CTE instead of a subquery."*
- Ask Copilot: *"What index would help this query run faster?"*

---

## Tip

If a query isn't quite right, **iterate**: tell Copilot what's wrong rather than starting over.  
*"The result includes NULL regions — exclude those."* is a valid follow-up.

---

## Done?

Check your answers against `challenges_solution.sql`, then move on to **Exercise 03 →**
