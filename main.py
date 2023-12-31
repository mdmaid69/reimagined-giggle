  import sqlite3
  def close_database_connection(connection):
        connection.close()
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)