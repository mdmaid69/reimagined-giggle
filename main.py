import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)