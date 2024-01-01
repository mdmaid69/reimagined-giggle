  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets