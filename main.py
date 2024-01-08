  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time