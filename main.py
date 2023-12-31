  import sqlite3
  def close_database_connection(connection):
        connection.close()
n = 10
print("Cube numbers:", [x**3 for x in range(n)])