  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)