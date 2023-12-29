  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))