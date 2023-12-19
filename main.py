  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps