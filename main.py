  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"