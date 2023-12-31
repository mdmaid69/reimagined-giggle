  import sqlite3
  def close_database_connection(connection):
        connection.close()
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)