  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import time
def get_current_time():
        return time.time()