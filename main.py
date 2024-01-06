import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
  import sqlite3
  def close_database_connection(connection):
        connection.close()