  import sqlite3
  def close_database_connection(connection):
        connection.close()
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a