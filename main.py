  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])