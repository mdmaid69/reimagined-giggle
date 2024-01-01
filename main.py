  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)