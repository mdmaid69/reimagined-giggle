n = 10
print("Powers of 2:", [2**x for x in range(n)])
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()