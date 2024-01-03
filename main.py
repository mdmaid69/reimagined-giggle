  import sqlite3
  def close_database_connection(connection):
        connection.close()
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))