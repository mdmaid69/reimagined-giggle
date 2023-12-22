def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)