  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)