  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()