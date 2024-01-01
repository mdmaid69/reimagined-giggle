import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
  import sqlite3
  def close_database_connection(connection):
        connection.close()