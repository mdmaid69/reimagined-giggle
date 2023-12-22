  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import array
def get_array_as_set(array):
        return set(array)