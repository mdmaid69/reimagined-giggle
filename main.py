  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()