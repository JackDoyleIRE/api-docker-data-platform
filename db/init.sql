-- Create the database
CREATE DATABASE example_database;

-- Connect to the database
\c example_database;

-- Create schemas if they don't exist
CREATE SCHEMA IF NOT EXISTS example_database_crm;
CREATE SCHEMA IF NOT EXISTS example_database_ecommerce;
CREATE SCHEMA IF NOT EXISTS example_database_analytics;


-- Creating customer schema
CREATE TABLE example_database.customers (
    id SERIAL PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    username VARCHAR(50),
    age INTEGER,
    company_department VARCHAR(100),
    company_name VARCHAR(100),
    outreaches JSONB
);

-- Create the purchases schema
CREATE TABLE example_database_ecommerce.purchases (
    id SERIAL PRIMARY KEY,
    customer_username VARCHAR(50),
    net_price FLOAT,
    gross_price FLOAT
);