import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
  import sqlite3
  def close_database_connection(connection):
        connection.close()