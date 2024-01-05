  import sqlite3
  def close_database_connection(connection):
        connection.close()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)