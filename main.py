import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()