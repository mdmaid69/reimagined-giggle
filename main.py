  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)