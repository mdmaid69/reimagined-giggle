import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)