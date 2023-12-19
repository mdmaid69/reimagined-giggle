def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)