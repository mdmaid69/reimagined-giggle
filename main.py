  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)