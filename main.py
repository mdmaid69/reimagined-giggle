n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)