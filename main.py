  import sqlite3
  def close_database_connection(connection):
        connection.close()
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)