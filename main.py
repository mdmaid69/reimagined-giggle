  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
  import sqlite3
  def close_database_connection(connection):
        connection.close()