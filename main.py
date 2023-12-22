import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()