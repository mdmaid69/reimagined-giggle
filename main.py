import array
def get_array_as_memoryview(array):
        return memoryview(array)
  import sqlite3
  def close_database_connection(connection):
        connection.close()