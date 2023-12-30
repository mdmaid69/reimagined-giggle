  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))