i = 0
while i < 5:
        print(i)
        i += 1
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)