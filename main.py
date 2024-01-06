def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
  import sqlite3
  def close_database_connection(connection):
        connection.close()