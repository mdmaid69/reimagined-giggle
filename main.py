  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
  import sqlite3
  def close_database_connection(connection):
        connection.close()