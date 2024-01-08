  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
  import sqlite3
  def close_database_connection(connection):
        connection.close()