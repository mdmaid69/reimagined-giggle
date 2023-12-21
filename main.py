  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
n = 10
print("Cube numbers:", [x**3 for x in range(n)])