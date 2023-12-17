numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
  import sqlite3
  def close_database_connection(connection):
        connection.close()