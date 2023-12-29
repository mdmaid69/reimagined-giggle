import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()