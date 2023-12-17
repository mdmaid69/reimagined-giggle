  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  import sqlite3
  def close_database_connection(connection):
        connection.close()