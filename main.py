  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)