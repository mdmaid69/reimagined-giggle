  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import os
def remove_directory(path):
        os.rmdir(path)