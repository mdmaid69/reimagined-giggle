  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_perpetuity(payment, rate):
        return payment / rate