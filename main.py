  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)