  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))