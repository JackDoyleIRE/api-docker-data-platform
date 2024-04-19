CREATE TABLE example_database_analytics.cost_revenue_ratio AS (
WITH outreach_by_customer AS (
    SELECT
        id, 
        firstname, 
        lastname,
        username,
        sum_cost
    FROM
        example_database_analytics.outreach_by_customer
),

net_purchase_prices AS (
    SELECT
        customer_username,
        total_net_price
    FROM
        example_database_analytics.net_purchase_prices
    )

SELECT 
    customer.firstname, 
    customer.lastname,
    ROUND(price.total_net_price) AS revenue,
    ROUND(customer.sum_cost, 2) AS cost,
    ROUND(customer.sum_cost / price.total_net_price::numeric, 2) as cost_revenue_ratio
FROM net_purchase_prices price
INNER JOIN outreach_by_customer customer
ON customer.username = price.customer_username)