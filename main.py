  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import array
def pop_from_array(array, i=-1):
        return array.pop(i)