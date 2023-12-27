  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)