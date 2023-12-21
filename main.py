  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize