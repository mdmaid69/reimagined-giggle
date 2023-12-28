  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)