def calculate_perpetuity(payment, rate):
        return payment / rate
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)