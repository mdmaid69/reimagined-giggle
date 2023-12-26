  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)