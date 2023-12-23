  import sqlite3
  def close_database_connection(connection):
        connection.close()
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)