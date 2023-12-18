  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)