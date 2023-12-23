  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
  import sqlite3
  def close_database_connection(connection):
        connection.close()