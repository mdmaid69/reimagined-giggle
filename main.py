  import sqlite3
  def close_database_connection(connection):
        connection.close()
import os
def get_environment_variable(var):
        return os.getenv(var)