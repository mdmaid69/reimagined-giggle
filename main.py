def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()