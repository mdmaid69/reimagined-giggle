  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)