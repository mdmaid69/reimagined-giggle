  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
def calculate_irr(cash_flows):
        rate = 0.1
        for _ in range(100):
        npv = sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
        if abs(npv) < 1e-6:
                return rate
        rate += 0.01
        return None