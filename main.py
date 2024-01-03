import os
def list_files_in_directory(path):
        return os.listdir(path)
  import sqlite3
  def close_database_connection(connection):
        connection.close()