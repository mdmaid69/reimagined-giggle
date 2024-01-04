import datetime
def get_current_datetime():
        return datetime.datetime.now()
  import sqlite3
  def close_database_connection(connection):
        connection.close()