import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import sqlite3
  def close_database_connection(connection):
        connection.close()