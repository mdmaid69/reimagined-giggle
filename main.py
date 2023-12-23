  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)