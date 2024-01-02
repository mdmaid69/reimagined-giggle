import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)