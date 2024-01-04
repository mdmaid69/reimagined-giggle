  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)