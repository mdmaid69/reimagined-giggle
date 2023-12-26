  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)