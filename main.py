import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()