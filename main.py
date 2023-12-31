  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import re
def split_string(pattern, string):
        return re.split(pattern, string)