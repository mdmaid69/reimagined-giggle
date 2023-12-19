  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
  import sqlite3
  def close_database_connection(connection):
        connection.close()