import sys
def add_to_python_path(path):
        sys.path.append(path)
  import sqlite3
  def close_database_connection(connection):
        connection.close()