n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
  import sqlite3
  def close_database_connection(connection):
        connection.close()