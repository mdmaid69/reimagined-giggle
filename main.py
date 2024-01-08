  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)