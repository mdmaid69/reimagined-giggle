import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()