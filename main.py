  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
n = 10
print("Square numbers:", [x**2 for x in range(n)])