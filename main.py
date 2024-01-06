  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
  import sqlite3
  def close_database_connection(connection):
        connection.close()