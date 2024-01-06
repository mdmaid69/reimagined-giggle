  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import sqlite3
  def close_database_connection(connection):
        connection.close()