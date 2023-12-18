def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()