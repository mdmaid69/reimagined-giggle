n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)