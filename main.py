  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
  import sqlite3
  def close_database_connection(connection):
        connection.close()