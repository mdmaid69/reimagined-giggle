  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import os
  def delete_file(file_name):
        os.remove(file_name)