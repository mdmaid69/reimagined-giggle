import math
def calculate_sign(x):
        return math.copysign(1, x)
  import sqlite3
  def close_database_connection(connection):
        connection.close()