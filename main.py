  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags