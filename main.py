import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()