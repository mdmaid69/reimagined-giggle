  import os
  def split_path(path):
        return os.path.split(path)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)