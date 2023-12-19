n = 10
print("Cube numbers:", [x**3 for x in range(n)])
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)