  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets