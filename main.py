import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()