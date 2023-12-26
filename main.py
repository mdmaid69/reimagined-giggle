  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities