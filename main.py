import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)