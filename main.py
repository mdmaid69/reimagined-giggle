numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)