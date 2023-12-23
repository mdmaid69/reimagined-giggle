import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()