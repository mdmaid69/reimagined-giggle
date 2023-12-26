def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
  import sqlite3
  def close_database_connection(connection):
        connection.close()