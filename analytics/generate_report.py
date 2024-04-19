from execute_sql import SQLExecutor
import csv

# Database credentials
dbname = "example_database"
user = "postgres"
password = "password"
host = "db"
port = "5432"

# Create SQLExecutor instance
executor = SQLExecutor(dbname, user, password, host, port)

# Connect to the database
executor.connect()

# Execute SQL files
sql_files = [
    "net_purchase_prices.sql",
    "outreach_by_customer.sql",
    "cost_revenue_ratio.sql"
]

for sql_file in sql_files:
    executor.execute_sql_file(sql_file)

# Reuse the existing database connection from the SQLExecutor instance
conn = executor.conn

# Query the table using psycopg2

cursor = conn.cursor()
cursor.execute("SELECT * FROM example_database_analytics.cost_revenue_ratio")
rows = cursor.fetchall()
print("Fetched data from the SQL table")


# Specify the output CSV file path
output_csv_path = 'output/cost_revenue_ratio.csv'

# Export data to CSV
try:
    with open(output_csv_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header
        csv_writer.writerow([desc[0] for desc in cursor.description])
        # Write rows
        csv_writer.writerows(rows)
    print("Data exported to CSV:", output_csv_path)
except Exception as e:
    print(f"Error exporting data to CSV: {e}")
    raise
finally:
    conn.close()
    print("Database connection closed")









