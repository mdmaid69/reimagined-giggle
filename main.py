  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)