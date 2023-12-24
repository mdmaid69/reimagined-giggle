  import sqlite3
  def close_database_connection(connection):
        connection.close()
import platform
def get_python_version():
        return platform.python_version()