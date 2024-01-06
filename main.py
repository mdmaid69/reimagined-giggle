import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()