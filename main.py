  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)