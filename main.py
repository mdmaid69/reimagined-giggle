  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)