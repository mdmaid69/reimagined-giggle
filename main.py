  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)