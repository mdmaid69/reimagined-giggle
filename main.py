import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()