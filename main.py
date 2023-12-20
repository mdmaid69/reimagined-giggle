  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding