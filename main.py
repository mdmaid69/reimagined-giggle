  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)