import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)