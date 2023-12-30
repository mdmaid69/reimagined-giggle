  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import os
def change_working_directory(path):
        os.chdir(path)