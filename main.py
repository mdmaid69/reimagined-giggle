import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)