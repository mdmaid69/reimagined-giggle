  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value