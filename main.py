  import sqlite3
  def close_database_connection(connection):
        connection.close()
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))