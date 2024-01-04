  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()