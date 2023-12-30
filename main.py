import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)