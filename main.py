def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)