  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity