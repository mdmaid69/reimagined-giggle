  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()