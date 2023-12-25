  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets