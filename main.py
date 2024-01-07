import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import sqlite3
  def close_database_connection(connection):
        connection.close()