import yaml
import json
from datetime import datetime
import psycopg2
from ingestion.operators.api_call_operator import ApiOperator
from ingestion.schemas.example_buisness_schema import CustomerObject, PurchaseObject
import os

# Load configuration from YAML file
with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

# Generalized function to connect to a database
def get_database_connection():
    db_config = config["database"]
    return psycopg2.connect(
        dbname=db_config["dbname"],
        user=db_config["user"],
        password=db_config["password"],
        host=db_config["host"],
        port=db_config["port"],
    )

def insert_data(cursor, table_name, data, schema_object):
    insert_statement = f"""
        INSERT INTO {table_name} ({', '.join(schema_object.columns)})
        VALUES ({', '.join(['%s'] * len(schema_object.columns))})
    """
    values = [getattr(data, column) for column in schema_object.columns]
    cursor.execute(insert_statement, values)

def main():
    # Read API key from the secret file
    with open("/run/secrets/api_key", "r") as f:
        api_key = f.read().strip()

    # Initialize ApiOperator with base URL and API key
    api_operator = ApiOperator("https://example-url.com/", api_key)

    # Get the current date in the desired format
    latest = datetime.now().strftime("%Y-%m-%d")

    conn = get_database_connection()
    cursor = conn.cursor()

    # Process each endpoint defined in the configuration file
    for endpoint in config["endpoints"]:
        # Call API for each endpoint
        api_operator.call_api_and_save_response(endpoint["endpoint"])

        # Construct the file path with the latest date
        file_path = f"{endpoint['file_path'].replace('.json', f'_{latest}.json')}"

        # Load JSON data from the file with the latest date
        with open(file_path, "r") as file:
            json_data = json.load(file)

        table_name = endpoint["table"]

        # Loop through the records and insert into the corresponding table
        for record in json_data.get(endpoint["name"], []):
            schema_object = globals()[endpoint["object"]](record)
            insert_data(cursor, table_name, schema_object, schema_object)

        conn.commit()

    cursor.close()
    conn.close()
    print("Ingestion complete")

if __name__ == "__main__":
    main()