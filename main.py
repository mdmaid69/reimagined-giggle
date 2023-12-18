import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)