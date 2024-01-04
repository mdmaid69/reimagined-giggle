import array
def set_array_item(array, i, item):
        array[i] = item
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)