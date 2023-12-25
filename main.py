  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]