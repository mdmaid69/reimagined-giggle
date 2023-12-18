  import os
  def get_base_name(path):
        return os.path.basename(path)
  import sqlite3
  def close_database_connection(connection):
        connection.close()