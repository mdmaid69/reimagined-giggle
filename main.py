  import sqlite3
  def close_database_connection(connection):
        connection.close()
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))