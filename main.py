  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)