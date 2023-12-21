n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)