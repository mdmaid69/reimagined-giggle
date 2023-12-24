  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)