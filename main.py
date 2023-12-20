  import os
  def split_path(path):
        return os.path.split(path)
  import sqlite3
  def close_database_connection(connection):
        connection.close()