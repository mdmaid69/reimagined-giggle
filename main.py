  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)