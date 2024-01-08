import time
def get_time_since_epoch():
        return time.time()
  import sqlite3
  def close_database_connection(connection):
        connection.close()