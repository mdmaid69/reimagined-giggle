  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)