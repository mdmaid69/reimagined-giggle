  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)