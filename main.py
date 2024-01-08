import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)