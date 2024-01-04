def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()