  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)