def calculate_energy(mass, c=3*10**8):
        return mass * c**2
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()