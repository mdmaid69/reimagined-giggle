  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)