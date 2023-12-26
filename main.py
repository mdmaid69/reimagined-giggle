  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)