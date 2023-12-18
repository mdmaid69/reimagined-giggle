  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)