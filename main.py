import math
def calculate_circle_area(radius):
        return math.pi * radius**2
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()