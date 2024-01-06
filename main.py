  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets