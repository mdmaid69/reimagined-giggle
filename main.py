def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)