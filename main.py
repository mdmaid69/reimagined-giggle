  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()