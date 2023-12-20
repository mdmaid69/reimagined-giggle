import itertools
print(list(itertools.permutations([1, 2, 3])))
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()