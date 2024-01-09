  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value