  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)