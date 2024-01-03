  import os
  def get_directory_name(path):
        return os.path.dirname(path)
  import sqlite3
  def close_database_connection(connection):
        connection.close()