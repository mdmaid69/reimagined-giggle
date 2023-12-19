import time
def get_current_time():
        return time.ctime()
  import sqlite3
  def close_database_connection(connection):
        connection.close()