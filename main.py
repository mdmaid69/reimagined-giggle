  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])