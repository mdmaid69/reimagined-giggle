  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()