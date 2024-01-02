  import math
  def calculate_square_root(n):
        return math.sqrt(n)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()