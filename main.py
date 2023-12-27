  import sqlite3
  def close_database_connection(connection):
        connection.close()
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)