  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
  import sqlite3
  def close_database_connection(connection):
        connection.close()