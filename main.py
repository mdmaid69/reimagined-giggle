  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
  import sqlite3
  def close_database_connection(connection):
        connection.close()