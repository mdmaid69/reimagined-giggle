  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()