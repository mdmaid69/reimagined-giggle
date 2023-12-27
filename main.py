  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True