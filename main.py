  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)