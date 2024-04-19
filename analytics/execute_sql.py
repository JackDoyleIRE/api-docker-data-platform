import psycopg2
from typing import Optional

class SQLExecutor:
    def __init__(self, dbname: str, user: str, password: str, host: str, port: int):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn: Optional[psycopg2.extensions.connection] = None  # Placeholder for the connection object

    def connect(self) -> None:
        """Establishes a connection to the database."""
        self.conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )

    def execute_sql_file(self, sql_file: str) -> None:
        """Executes SQL queries from a file."""
        if self.conn is None:
            self.connect()  # Ensure connection is established

        cursor = self.conn.cursor()

        # Execute SQL file
        with open(sql_file, "r") as file:
            query = file.read()
            cursor.execute(query)

        # Commit and close connection
        self.conn.commit()
        cursor.close()




