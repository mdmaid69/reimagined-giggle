  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal