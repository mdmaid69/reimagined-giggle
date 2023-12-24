  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))