import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  import sqlite3
  def close_database_connection(connection):
        connection.close()