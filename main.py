import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)