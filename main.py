  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()