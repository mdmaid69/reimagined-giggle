  import sqlite3
  def close_database_connection(connection):
        connection.close()
import platform
def get_os_info():
        return platform.uname()