  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
  import sqlite3
  def close_database_connection(connection):
        connection.close()