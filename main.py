  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))