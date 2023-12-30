  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]