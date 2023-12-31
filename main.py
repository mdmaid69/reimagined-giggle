import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()