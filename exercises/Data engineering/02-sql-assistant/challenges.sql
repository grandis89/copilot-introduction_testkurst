-- ============================================================
-- Exercise 02 — SQL Challenges
-- ============================================================
-- For each challenge, use Copilot Chat to write the query.
-- Paste your answer below each comment block.
-- Reference schema is in schema.sql.
-- ============================================================


-- ------------------------------------------------------------
-- Challenge 1: Total revenue per region
-- Business question:
--   What is the total revenue generated in each region?
--   Show region and total_revenue, ordered from highest to lowest.
--   Revenue = quantity * unit_price * (1 - discount_pct / 100)
-- ------------------------------------------------------------



-- ------------------------------------------------------------
-- Challenge 2: Top 5 customers by number of orders
-- Business question:
--   Which 5 customers have placed the most orders?
--   Show customer_name, region, and order_count.
-- ------------------------------------------------------------



-- ------------------------------------------------------------
-- Challenge 3: Monthly revenue trend
-- Business question:
--   Show total revenue for each month in 2025,
--   formatted as YYYY-MM, ordered chronologically.
-- ------------------------------------------------------------



-- ------------------------------------------------------------
-- Challenge 4: Best-selling product per category
-- Business question:
--   For each product category, which product generated
--   the highest total revenue? Show category, product_name,
--   and total_revenue. (Hint: window functions may help)
-- ------------------------------------------------------------



-- ------------------------------------------------------------
-- Challenge 5: Optimise this slow query
-- The query below works but is slow on a large orders table.
-- Ask Copilot what is wrong and how to fix it.
-- ------------------------------------------------------------

-- SLOW QUERY (do not change this block — just ask Copilot to analyse it):
SELECT
    c.customer_name,
    c.region,
    (
        SELECT SUM(o2.quantity * p2.unit_price)
        FROM orders o2
        JOIN products p2 ON o2.product_id = p2.product_id
        WHERE o2.customer_id = c.customer_id
    ) AS total_revenue
FROM customers c
ORDER BY total_revenue DESC;

-- YOUR OPTIMISED VERSION:
