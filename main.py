  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)