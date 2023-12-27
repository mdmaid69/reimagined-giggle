  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)