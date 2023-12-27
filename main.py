def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()