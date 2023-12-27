def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)