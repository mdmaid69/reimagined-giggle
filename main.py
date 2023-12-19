  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
  import sqlite3
  def close_database_connection(connection):
        connection.close()