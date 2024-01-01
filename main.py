  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
  import sqlite3
  def close_database_connection(connection):
        connection.close()