import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
  import sqlite3
  def close_database_connection(connection):
        connection.close()