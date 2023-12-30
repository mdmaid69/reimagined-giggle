  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)