  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
  import sqlite3
  def close_database_connection(connection):
        connection.close()