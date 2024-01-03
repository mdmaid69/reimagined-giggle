numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()