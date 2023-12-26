import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
  import sqlite3
  def close_database_connection(connection):
        connection.close()