import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()