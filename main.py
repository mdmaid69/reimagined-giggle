import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()