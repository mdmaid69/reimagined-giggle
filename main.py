  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
  import sqlite3
  def close_database_connection(connection):
        connection.close()