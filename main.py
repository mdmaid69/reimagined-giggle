  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
  import sqlite3
  def close_database_connection(connection):
        connection.close()