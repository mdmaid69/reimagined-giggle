  import sqlite3
  def close_database_connection(connection):
        connection.close()
import os
def change_working_directory(path):
        os.chdir(path)