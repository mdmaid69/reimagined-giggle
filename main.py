  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)