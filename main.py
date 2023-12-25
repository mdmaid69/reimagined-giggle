  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
  import sqlite3
  def close_database_connection(connection):
        connection.close()