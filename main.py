import math
def calculate_gamma_function(x):
        return math.gamma(x)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()