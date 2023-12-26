  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)