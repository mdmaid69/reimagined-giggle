def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()