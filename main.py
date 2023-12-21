def calculate_average(numbers):
        return sum(numbers) / len(numbers)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()