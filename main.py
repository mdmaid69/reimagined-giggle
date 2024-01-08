  import sqlite3
  def close_database_connection(connection):
        connection.close()
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])