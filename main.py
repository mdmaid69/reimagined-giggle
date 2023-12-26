def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)