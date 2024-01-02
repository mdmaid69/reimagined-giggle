import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)