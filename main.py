  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)