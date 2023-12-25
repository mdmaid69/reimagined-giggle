import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()