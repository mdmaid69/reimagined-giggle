  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)