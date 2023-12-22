def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)