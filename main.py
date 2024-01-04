def is_odd(n):
        return n % 2 != 0
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)