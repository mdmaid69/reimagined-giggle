import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
  import sqlite3
  def close_database_connection(connection):
        connection.close()