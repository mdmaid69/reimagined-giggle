def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()