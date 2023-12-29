  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import array
def append_to_array(array, item):
        array.append(item)