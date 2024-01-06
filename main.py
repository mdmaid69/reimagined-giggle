  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)