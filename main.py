  import sqlite3
  def close_database_connection(connection):
        connection.close()
import array
def get_array_as_bytes(array):
        return bytes(array)