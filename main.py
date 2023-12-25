import math
def calculate_logarithm_base_2(x):
        return math.log2(x)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()