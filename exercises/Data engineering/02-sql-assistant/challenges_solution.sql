-- ============================================================
-- Exercise 02 — SQL Challenges: Reference Solutions
-- ============================================================


-- Challenge 1: Total revenue per region
SELECT
    c.region,
    ROUND(SUM(o.quantity * p.unit_price * (1 - o.discount_pct / 100)), 2) AS total_revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p  ON o.product_id  = p.product_id
GROUP BY c.region
ORDER BY total_revenue DESC;


-- Challenge 2: Top 5 customers by number of orders
SELECT
    c.customer_name,
    c.region,
    COUNT(o.order_id) AS order_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name, c.region
ORDER BY order_count DESC
LIMIT 5;


-- Challenge 3: Monthly revenue trend (2025)
SELECT
    TO_CHAR(o.order_date, 'YYYY-MM') AS month,
    ROUND(SUM(o.quantity * p.unit_price * (1 - o.discount_pct / 100)), 2) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.order_date BETWEEN '2025-01-01' AND '2025-12-31'
GROUP BY TO_CHAR(o.order_date, 'YYYY-MM')
ORDER BY month;


-- Challenge 4: Best-selling product per category (window function)
WITH revenue_per_product AS (
    SELECT
        p.category,
        p.product_name,
        ROUND(SUM(o.quantity * p.unit_price * (1 - o.discount_pct / 100)), 2) AS total_revenue,
        RANK() OVER (PARTITION BY p.category ORDER BY SUM(o.quantity * p.unit_price) DESC) AS rnk
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY p.category, p.product_id, p.product_name
)
SELECT category, product_name, total_revenue
FROM revenue_per_product
WHERE rnk = 1
ORDER BY category;


-- Challenge 5: Optimised version (replace correlated subquery with a JOIN)
SELECT
    c.customer_name,
    c.region,
    ROUND(SUM(o.quantity * p.unit_price * (1 - o.discount_pct / 100)), 2) AS total_revenue
FROM customers c
JOIN orders o   ON o.customer_id = c.customer_id
JOIN products p ON o.product_id  = p.product_id
GROUP BY c.customer_id, c.customer_name, c.region
ORDER BY total_revenue DESC;
