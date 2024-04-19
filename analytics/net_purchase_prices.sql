CREATE TABLE mock_company_analytics.net_purchase_prices as (

SELECT 
    customer_username,
    SUM(net_price) AS total_net_price
FROM 
    mock_company_ecommerce.purchases
GROUP BY customer_username)