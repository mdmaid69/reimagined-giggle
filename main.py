  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)