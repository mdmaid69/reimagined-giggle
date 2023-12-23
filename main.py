  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()