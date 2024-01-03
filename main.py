  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
  import sqlite3
  def close_database_connection(connection):
        connection.close()