  import sqlite3
  def close_database_connection(connection):
        connection.close()
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])