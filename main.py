  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)