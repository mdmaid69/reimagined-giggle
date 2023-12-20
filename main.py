  import sqlite3
  def close_database_connection(connection):
        connection.close()
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b