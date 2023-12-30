  import sqlite3
  def close_database_connection(connection):
        connection.close()
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a