  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
  import sqlite3
  def close_database_connection(connection):
        connection.close()