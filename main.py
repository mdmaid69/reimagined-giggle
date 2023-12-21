  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)