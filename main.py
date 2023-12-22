import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
  import sqlite3
  def close_database_connection(connection):
        connection.close()