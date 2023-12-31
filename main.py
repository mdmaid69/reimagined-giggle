import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()