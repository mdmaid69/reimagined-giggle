import math
def calculate_logarithm_base_10(x):
        return math.log10(x)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()