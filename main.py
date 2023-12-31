def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)