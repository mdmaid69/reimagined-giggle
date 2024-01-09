  import os
  def get_directory_name(path):
        return os.path.dirname(path)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()