  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import sqlite3
  def close_database_connection(connection):
        connection.close()