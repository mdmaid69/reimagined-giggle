  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()