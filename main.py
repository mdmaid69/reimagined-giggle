  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)