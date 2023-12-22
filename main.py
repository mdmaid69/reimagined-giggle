  import sqlite3
  def close_database_connection(connection):
        connection.close()
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a