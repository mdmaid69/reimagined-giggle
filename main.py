import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()