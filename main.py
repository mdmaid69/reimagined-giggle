def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()