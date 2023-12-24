def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import sqlite3
  def close_database_connection(connection):
        connection.close()