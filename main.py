import math
def calculate_absolute_value(x):
        return math.fabs(x)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()