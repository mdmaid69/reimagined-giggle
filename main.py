  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)