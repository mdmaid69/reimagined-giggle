def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
  import sqlite3
  def close_database_connection(connection):
        connection.close()