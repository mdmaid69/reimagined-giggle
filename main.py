import os
def remove_directory(path):
        os.rmdir(path)
  import sqlite3
  def close_database_connection(connection):
        connection.close()