n = 10
print("Square numbers:", [x**2 for x in range(n)])
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()