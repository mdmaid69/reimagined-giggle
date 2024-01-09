  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
  import sqlite3
  def close_database_connection(connection):
        connection.close()