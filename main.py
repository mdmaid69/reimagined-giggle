  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))