n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)