  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])