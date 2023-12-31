  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)