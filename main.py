import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)