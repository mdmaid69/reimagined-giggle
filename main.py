  def calculate_area_triangle(b, h):
        return 0.5 * b * h
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()