  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])