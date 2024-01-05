  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)