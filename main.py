  import sqlite3
  def close_database_connection(connection):
        connection.close()
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable