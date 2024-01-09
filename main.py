  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)