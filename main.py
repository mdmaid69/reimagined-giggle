  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()