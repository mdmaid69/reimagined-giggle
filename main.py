import array
def get_array_as_frozenset(array):
        return frozenset(array)
  import sqlite3
  def close_database_connection(connection):
        connection.close()