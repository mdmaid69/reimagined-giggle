  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)