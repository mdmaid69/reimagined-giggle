import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()