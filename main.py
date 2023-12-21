  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)