import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)