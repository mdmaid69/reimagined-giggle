  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  import sqlite3
  def close_database_connection(connection):
        connection.close()