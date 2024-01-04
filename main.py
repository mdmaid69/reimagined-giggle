  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()