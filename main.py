import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()