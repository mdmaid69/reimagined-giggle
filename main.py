def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()