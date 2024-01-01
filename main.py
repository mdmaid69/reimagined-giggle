  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]