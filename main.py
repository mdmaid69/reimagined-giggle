import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import sqlite3
  def close_database_connection(connection):
        connection.close()