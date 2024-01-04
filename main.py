  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)