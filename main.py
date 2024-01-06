def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)