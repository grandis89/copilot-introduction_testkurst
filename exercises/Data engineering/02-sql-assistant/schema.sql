-- ============================================================
-- Schema: Sales Reporting Database
-- ============================================================
-- Three tables: customers, products, orders
-- Use this schema as context when asking Copilot for queries.
-- ============================================================

CREATE TABLE customers (
    customer_id   VARCHAR(10)  PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    region        VARCHAR(50)  NOT NULL,
    signup_date   DATE         NOT NULL
);

CREATE TABLE products (
    product_id   INT          PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category     VARCHAR(50)  NOT NULL,
    unit_price   DECIMAL(10, 2) NOT NULL
);

CREATE TABLE orders (
    order_id     VARCHAR(10)   PRIMARY KEY,
    customer_id  VARCHAR(10)   NOT NULL REFERENCES customers(customer_id),
    product_id   INT           NOT NULL REFERENCES products(product_id),
    quantity     INT           NOT NULL CHECK (quantity > 0),
    order_date   DATE          NOT NULL,
    discount_pct DECIMAL(5, 2) DEFAULT 0.00  -- percentage discount, e.g. 10.00 = 10%
);
