import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import sqlite3
  def close_database_connection(connection):
        connection.close()