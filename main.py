import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()