  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  import sqlite3
  def close_database_connection(connection):
        connection.close()