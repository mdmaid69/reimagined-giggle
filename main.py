def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()