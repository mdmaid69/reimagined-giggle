  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
  import sqlite3
  def close_database_connection(connection):
        connection.close()