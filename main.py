  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import os
  def get_current_working_directory():
        return os.getcwd()