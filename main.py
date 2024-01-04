  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()