def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()