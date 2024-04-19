CREATE TABLE example_database_analytics.outreach_by_customer as (
WITH customer_data AS (
    SELECT 
        id, 
        firstname, 
        lastname, 
        username,
        REPLACE(jsonb_array_elements(outreaches)->>'cost', ',', '.')::numeric as cost
    FROM example_database_crm.customers
    WHERE company_department = 'Legal'
)

SELECT 
    id, 
    firstname, 
    lastname,
    username,
    sum(cost) as sum_cost
FROM 
    customer_data
GROUP BY 
    id, 
    firstname, 
    lastname,
    username)