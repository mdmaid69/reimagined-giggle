import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
  import sqlite3
  def close_database_connection(connection):
        connection.close()