  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
  import sqlite3
  def close_database_connection(connection):
        connection.close()