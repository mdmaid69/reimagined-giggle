import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  import sqlite3
  def close_database_connection(connection):
        connection.close()