import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)