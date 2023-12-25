import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import sqlite3
  def close_database_connection(connection):
        connection.close()