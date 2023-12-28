  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)