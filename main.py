  import sqlite3
  def close_database_connection(connection):
        connection.close()
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)