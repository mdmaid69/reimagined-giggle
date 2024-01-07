  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities