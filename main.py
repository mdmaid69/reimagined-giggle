  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import array
def iterate_over_array(array):
        for item in array:
        print(item)