  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)