import re
def split_string(pattern, string):
        return re.split(pattern, string)
  import sqlite3
  def close_database_connection(connection):
        connection.close()