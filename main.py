import datetime
def get_today_date():
        return datetime.date.today()
  import sqlite3
  def close_database_connection(connection):
        connection.close()