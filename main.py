  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)