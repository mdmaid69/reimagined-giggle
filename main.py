  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_average(numbers):
        return sum(numbers) / len(numbers)