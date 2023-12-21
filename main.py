  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import datetime
def get_current_datetime():
        return datetime.datetime.now()