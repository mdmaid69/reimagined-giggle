import os
def get_file_size(filename):
        return os.path.getsize(filename)
  import sqlite3
  def close_database_connection(connection):
        connection.close()