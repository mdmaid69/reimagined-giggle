  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)