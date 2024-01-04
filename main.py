  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b