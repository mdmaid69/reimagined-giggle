import array
def insert_into_array(array, i, item):
        array.insert(i, item)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)