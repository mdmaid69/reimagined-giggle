  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)