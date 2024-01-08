import datetime
def get_current_date():
        return datetime.date.today()
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)