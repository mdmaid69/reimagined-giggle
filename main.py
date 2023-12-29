  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)