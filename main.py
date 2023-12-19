  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time