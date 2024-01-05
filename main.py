  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)