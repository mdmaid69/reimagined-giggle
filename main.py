  import os
  def delete_file(file_name):
        os.remove(file_name)
  import sqlite3
  def close_database_connection(connection):
        connection.close()