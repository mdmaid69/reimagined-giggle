  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)