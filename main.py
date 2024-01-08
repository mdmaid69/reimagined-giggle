  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()