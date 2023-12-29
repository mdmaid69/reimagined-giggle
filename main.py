  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()