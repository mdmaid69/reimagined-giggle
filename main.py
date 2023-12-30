import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)