  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
for i in range(5):
        print(i)