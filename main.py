  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities