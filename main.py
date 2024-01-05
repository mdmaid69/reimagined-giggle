import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  import sqlite3
  def close_database_connection(connection):
        connection.close()