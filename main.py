  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
  import sqlite3
  def close_database_connection(connection):
        connection.close()