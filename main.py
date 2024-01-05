import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()