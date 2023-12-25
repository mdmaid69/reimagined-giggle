import os
def get_file_size(filename):
        return os.path.getsize(filename)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)