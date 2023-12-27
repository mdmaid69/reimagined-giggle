  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)