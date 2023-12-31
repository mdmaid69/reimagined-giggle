  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
  import sqlite3
  def close_database_connection(connection):
        connection.close()