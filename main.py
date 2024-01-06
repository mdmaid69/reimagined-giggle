  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)