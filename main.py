  import sqlite3
  def close_database_connection(connection):
        connection.close()
n = 10
print("Square numbers:", [x**2 for x in range(n)])