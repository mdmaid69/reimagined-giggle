  def remove_duplicates(lst):
        return list(set(lst))
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)