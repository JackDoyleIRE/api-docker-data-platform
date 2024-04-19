from api_operator import ApiOperator
import json
from datetime import datetime
import psycopg2
from schema import CustomerObject, PurchaseObject


import os

# Base URL for the api call
BASE_URL = "https://example-url.com/"

def main():
    # Path to the secret file inside the container
    SECRET_FILE_PATH = "/run/secrets/api_key"

    # Read API key from the secret file
    with open(SECRET_FILE_PATH, "r") as f:
        api_key = f.read().strip()
    
    # Initialize ApiOperator with base URL and API key
    api_operator = ApiOperator(BASE_URL, api_key)

    endpoints = ['endpoint_1', 'endpoint2']

    # Call API for each endpoint
    for endpoint in endpoints:
        api_operator.call_api_and_save_response(endpoint)

    # Get the current date in the desired format
    latest = datetime.now().strftime("%Y-%m-%d")

    # Construct the file path with the latest date
    file_path = f"object_store/crm_customers_{latest}.json"

    # Load JSON data from the file with the latest date
    with open(file_path, 'r') as file:
        json_data = json.load(file)

    # TODO Create a generalized connection method for the whole project, avoid hard coded credentials
        
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="mock_company",
        user="postgres",
        password="password",
        host="db",
        port="5432"
    )

    # Create a cursor object using the cursor() method
    cursor = conn.cursor()

    table_name = 'mock_company_crm.customers'

    # For each record in the data 
    for customer_data in json_data['customers']:
        customer = CustomerObject(customer_data)

        # Constuct the insert statment based on our desired schema size (see also db/init.sql)
        insert_statement = f"""
            INSERT INTO {table_name} ({', '.join(CustomerObject.columns)})
            VALUES ({', '.join(['%s'] * len(CustomerObject.columns))})
        """

        # Extract values from the customer object
        values = [getattr(customer, column) for column in CustomerObject.columns]

        # Execute the INSERT statement, passing in the values
        cursor.execute(insert_statement, values)

    # Commit the transaction
    conn.commit()
    print('customer data loaded to db')

    # TODO The code below is repetitive and hard coded so should be added to the database utility as a general insert method

    # Construct the file path with the latest date
    file_path = f"object_store/ecommerce_purchases_{latest}.json"

    # Load JSON data from the file with the latest date
    with open(file_path, 'r') as file:
        json_data = json.load(file)

    table_name = 'mock_company_ecommerce.purchases'

    for purchase_data in json_data['purchases']:
        purchase = PurchaseObject(purchase_data)
    
        insert_statement = f"""
            INSERT INTO {table_name} ({', '.join(PurchaseObject.columns)})
            VALUES ({', '.join(['%s'] * len(PurchaseObject.columns))})
        """

        # Extract values from the purchase object
        values = [getattr(purchase, column) for column in PurchaseObject.columns]

        # Execute the INSERT statement, passing in the values
        cursor.execute(insert_statement, values)
    
    conn.commit()
    print('Purchase data loaded to db')

    # Close the cursor and database connection
    cursor.close()
    conn.close()
    print('Ingestion complete')


if __name__ == "__main__":
    main()