  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
  import sqlite3
  def close_database_connection(connection):
        connection.close()