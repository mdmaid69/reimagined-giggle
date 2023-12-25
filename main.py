  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)